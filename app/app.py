import os
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "orders"),
    "user": os.getenv("DB_USER", "shopease"),
    "password": os.getenv("DB_PASSWORD", "shopease123"),
}


def get_conn():
    return psycopg2.connect(**DB_CONFIG)


@app.get("/api/health")
def health():
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1")
            return jsonify(status="ok", database="connected")
    except Exception as exc:
        return jsonify(status="degraded", database=str(exc)), 503


@app.get("/api/orders")
def list_orders():
    with get_conn() as conn, conn.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cur:
        cur.execute(
            "SELECT id, customer, item, quantity, status "
            "FROM orders ORDER BY id"
        )
        return jsonify(cur.fetchall())


@app.get("/api/orders/<int:order_id>")
def get_order(order_id):
    with get_conn() as conn, conn.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cur:
        cur.execute(
            "SELECT id, customer, item, quantity, status "
            "FROM orders WHERE id = %s",
            (order_id,),
        )

        row = cur.fetchone()

        if row is None:
            return jsonify(error="order not found"), 404

        return jsonify(row)


@app.post("/api/orders")
def create_order():
    data = request.get_json(silent=True) or {}

    missing = [
        f for f in ("customer", "item", "quantity")
        if f not in data
    ]

    if missing:
        return jsonify(
            error=f"missing fields: {', '.join(missing)}"
        ), 400

    with get_conn() as conn, conn.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cur:
        cur.execute(
            "INSERT INTO orders (customer, item, quantity) "
            "VALUES (%s, %s, %s) "
            "RETURNING id, customer, item, quantity, status",
            (
                data["customer"],
                data["item"],
                int(data["quantity"]),
            ),
        )

        return jsonify(cur.fetchone()), 201


@app.patch("/api/orders/<int:order_id>")
def update_status(order_id):
    status = (request.get_json(silent=True) or {}).get("status")

    if status not in (
        "PLACED",
        "PACKED",
        "SHIPPED",
        "DELIVERED",
    ):
        return jsonify(
            error="status must be PLACED, PACKED, SHIPPED or DELIVERED"
        ), 400

    with get_conn() as conn, conn.cursor(
        cursor_factory=psycopg2.extras.RealDictCursor
    ) as cur:
        cur.execute(
            "UPDATE orders SET status = %s WHERE id = %s "
            "RETURNING id, customer, item, quantity, status",
            (status, order_id),
        )

        row = cur.fetchone()

        if row is None:
            return jsonify(error="order not found"), 404

        return jsonify(row)
