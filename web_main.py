from aiohttp import web
import aiohttp_cors
from web.route.route import setup_routes


async def start_init_test(app):
    print("初始化操作")


async def end_init_test(app):
    print("清理操作")


def main():
    app = web.Application()
    setup_routes(app)
    app.on_startup.append(start_init_test)
    app.on_cleanup.append(end_init_test)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    web.run_app(app)



if __name__ == "__main__":
    main()