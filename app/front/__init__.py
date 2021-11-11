from flask import Blueprint
from flask_restful import Api


front_bp = Blueprint('front_bp', __name__)
front_api = Api(front_bp)

from . import analytics
from . import send_tg_notification
from . import users


front_api.add_resource(analytics.Analytics, '/api/v1/analytics/')
front_api.add_resource(send_tg_notification.SendTelegramNotification,
                       '/api/v1/send_telegram_notification/')
front_api.add_resource(users.UsersList, '/api/v1/users/')
front_api.add_resource(users.UserItem, '/api/v1/users/<int:telegram_id>/')
