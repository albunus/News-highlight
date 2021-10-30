import os

class Config:
   
   	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=42760c46e8c44cd0a71e4ec9374b4e0f'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-10-30&sortBy=popularity&apiKey=API_KEY'
   	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}