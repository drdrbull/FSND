from api.api import app

'''
db_drop_and_create_all()
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)