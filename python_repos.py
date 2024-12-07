import requests
import plotly.express as px
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers ={"Accept":"application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
repo_links,stars,hover_texts=[],[],[]
print(f"Repositories returned: {len(repo_dicts)}")

# repo_dict = repo_dicts[0]
# print(f"\nKeys:{len(repo_dicts)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# print("\nselected information about first repository:")
for repo_dict in repo_dicts:
    repo_name=repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner =repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)
#     print(f"name:{repo_dict['name']}")
#     print(f"owner:{repo_dict['owner']['login']}")
#     print(f"stars:{repo_dict['stargazers_count']}")
#     print(f"repository:{repo_dict['html_url']}")
#     print(f"created_at:{repo_dict['created_at']}")
#     print(f"updated_at:{repo_dict['updated_at']}")
#     print(f"description:{repo_dict['description']}")
#     print("\n\n")
# print(response_dict.keys())
title =("Most-Starred Python Projects on GitHub")
labels = {'x':'repository','y':'stars'}

fig = px.bar(x=repo_links,y=stars,title=title,labels=labels,hover_name=hover_texts)
fig.update_layout(title_font_size=28,xaxis_title_font_size =20,yaxis_title_font_size= 20)
fig.update_traces(marker_color = "SteelBlue",marker_opacity = 0.6)
fig.write_html('API.html')
# fig.show()