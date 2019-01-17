from water_inspect import app
from flask_apscheduler import APScheduler
from water_inspect.utils.fetch import fetch_check



if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.api_enabled = True
    print("Let us run out of the loop")
    scheduler.init_app(app)
    Fetch = fetch_check()
    scheduler.add_job(id ="job1", func=Fetch.accquir, args=(), trigger='interval', seconds=8)
    scheduler.start()
    app.run(debug=True,port = 80, host = "0.0.0.0")
