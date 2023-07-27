from polygon import RESTClient

client = RESTClient("uLM7HgvNyX6p0k9e79wlar8uVCCrFZb_")

# aggs = []
# for a in client.list_aggs(
#     "AAPL",
#     1,
#     "hour",
#     "2023-01-01",
#     "2023-01-02",
#     limit=2,
# ):
#     aggs.append(a)

# print(aggs)

aggs = client.get_aggs(
    "TSLA", 
    1,
    "day",
    "2023-07-25",
    "2023-07-27"
)

print(aggs.open)