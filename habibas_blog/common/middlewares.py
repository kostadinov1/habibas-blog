def last_viewed_posts(get_response):
    def middleware(request):
        request.last_viewed_posts = request.session.get('last_viewed_posts')
        return get_response(request)

    return middleware
