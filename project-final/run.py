from backend.app import app

if __name__ == '__main__':
    print("Starting Flask server...")
    print("Server will be available at: http://127.0.0.1:8080")
    app.run(host='127.0.0.1', port=8080) 