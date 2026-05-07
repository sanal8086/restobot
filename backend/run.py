from app import create_app

app = create_app()

if __name__ == '__main__':
    # No seeding needed as it will be handled by the admin portal
    app.run(host='0.0.0.0', debug=True, port=5000)
