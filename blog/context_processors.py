from blog.models import Article, Tags


def blog(request):
    tags = Tags.objects.all()
    dates = Article.objects.datetimes('pub_time', 'month', order='DESC')

    return {
        'tags': tags,
        'dates': dates,
    }
