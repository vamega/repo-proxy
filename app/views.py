from aiohttp import web
from aiohttp_jinja2 import template

@template('index.jinja')
async def index(request):
    """
    This is the view handler for the "/" url.

    :param request: the request object see http://aiohttp.readthedocs.io/en/stable/web_reference.html#request
    :return: context for the template.
    """
    # Note: we return a dict not a response because of the @template decorator
    return {
        'title': request.app['name'],
        'intro': "Success! you've setup a basic aiohttp app.",
    }


async def reverse_proxy_no_cache(request):
    print("No cache on.")
    remote_url_part = request.match_info['url']
    remote_url ='https://conda.anaconda.org/conda-forge/{}'.format(remote_url_part)
    print(remote_url_part)
    print(remote_url)
    client_session = request.app['client_session']
    remote_response = await client_session.get(remote_url)
    remote_response_txt= await remote_response.text()
    return web.Response(text=remote_response_txt)

async def reverse_proxy(request):
    print(request.match_info['url'])
    return web.Response()
