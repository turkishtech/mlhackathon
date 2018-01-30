import csv
import pickle

csv_data  = []

# file to load data from
csv_file = 'telekom_hilft/telekom_hilft_comments.csv'

# create list of dictionaries
"""
with open(csv_file) as comments_csv:
    reader = csv.reader(comments_csv, delimiter=";", quotechar="|")
    for index, row in enumerate(reader):
        if index != 0:
            data = {'position': row[0], 'post_id':row[1], 'post_by':row[2], 'post_text': row[3],
            'post_published': row[4], 'comment_id': row[5], 'comment_by': row[6], 'is_replay':row[7],
            'comment_message': row[8], 'comment_published': row[9], 'comment_like_count':row[10]}
            csv_data.append(data)
"""

# save csv data as pickle_file
#pickle.dump(csv_data, open('comments.p', 'wb'))

# load data
csv_data = pickle.load(open("comments.p", "rb"))

# csv_file dict ordered by post_id
"""Structure:
<post_id>:{'text':<post_text>, 'comments':[comment1, comment2, ...]}

"""
csv_data_posts = dict()
for index, entry in enumerate(csv_data):
    if entry['post_id'] in csv_data_posts.keys():
        csv_data_posts[entry['post_id']]['comments'].append(entry['comment_message'])
    else:
        csv_data_posts[entry['post_id']] = {'text': entry['post_text'], 'comments':[entry['comment_message']]}

# loop through all the posts, extracting comments and post text
for index, post_data in enumerate(csv_data_posts.items()):
    post_number = index
    key = post_data[0]
    post_text = post_data[1]['text']
    post_comments = post_data[1]['comments']

with open('posts_csv') as posts_csv:
    writer = csv.writer(posts_csv)
    for key, value in csv_data.items():
        writer.writerow([key, value])
