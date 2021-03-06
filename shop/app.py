from shop.api import create_app
from shop.api.settings import ProdConfig

app = create_app(ProdConfig)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
