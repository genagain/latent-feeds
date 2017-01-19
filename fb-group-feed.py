import os
import facebook

access_token = os.environ['FB_ACCESS_TOKEN']

graph = facebook.GraphAPI(access_token = access_token, version='2.5')
feed = graph.get_object(id='1525861407646621', fields='feed')['feed']
post_ids = map(lambda post: post['id'], feed['data'])
post_links = map(lambda post_id: graph.get_object(id=post_id, fields='link,created_time'), post_ids)
print post_links
