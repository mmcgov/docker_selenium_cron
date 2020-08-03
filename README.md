# docker_compose_selenium_cron

## Quick start guide:
NOTE: This docker has been setup with the example case of logging into flyefit website and automatically booking a gym class but with small tweaks it could easily be used for any situation where you want to periodically scrape/interact with a website using selenium. The regular job is setup via a cron job.
<br>
1) Git clone this repo
2) Move the env file to `.env`
3) change the email and password variables in this `.env` file to your personal values.
4) change the time of gym class you want to book the next day. This time is set inside the scraping script gym_scheduler.py
5) Finally `docker-compose up` and the docker should regularly book the chosne class according to the cron schedule.

## Summary
This docker-compose project is designed to streamline the process of running a regular job such as scraping periodically via a cron schedule. as it is setup via docker-compose it is easy to add on additional services which interact with this selenium process. (See my docker_nginx_certbot_dash_scrapy_cron repo).
