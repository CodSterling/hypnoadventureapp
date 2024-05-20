import aiohttp
import aiohttp.web
import random
import os


async def left(request):
    outcomes = ["pass", "blocked", "trapped", "door"]
    outcome = random.choice(outcomes)
    path = request.match_info.get('path', "unknown")
    result = ""
    if outcome == "pass":
        result = ("You pass through the path without any issues.\n"
                  "Use .left, .right, .up or .down to proceed!")
    elif outcome == "blocked":
        result = ("The path is blocked by a large boulder.\n"
                  "Use .left, .right, .up or .down to proceed!")
    elif outcome == "trapped":
        result = "You are TRAPPED!\n Use .free to FREE YOURSELF!"
    elif outcome == "door":
        result = ("You find a mysterious door on the path.\n"
                  "Use .wakeup to help Cod WAKE UP!")
    return aiohttp.web.Response(text=result)


# Define the async function handle to serve the HTML file
async def path_handler(request):
    # Path to the index.html file
    file_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')

    with open(file_path, 'r') as file:
        content = file.read()

    return aiohttp.web.Response(text=content, content_type='text/html')


# Create an application instance and define routes
app = aiohttp.web.Application()
app.router.add_get('/', path_handler)
app.router.add_get('/path/{path}', path_handler)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    aiohttp.web.run_app(app, port=port)