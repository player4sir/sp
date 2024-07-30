import json
from spankbang_api.spankbang_api import Client


def handler(event, context):
    try:
        client = Client()
        query = event.get('queryStringParameters', {}).get(
            'query', 'default_query')
        video = client.get_video(query)
        if video:
            video_data = {
                "title": video.title,
                "author": video.author,
                "length": video.length,
                "publish_date": video.publish_date,
                "tags": video.tags,
                "video_qualities": video.video_qualities,
                "direct_download_urls": video.direct_download_urls,
                "thumbnail": video.thumbnail,
                "description": video.description,
                "embed_url": video.embed_url,
                "rating": video.rating,
            }
            return {
                "statusCode": 200,
                "body": json.dumps(video_data)
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Video not found"})
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
