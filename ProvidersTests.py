import g4f
from g4f import set_cookies

# Print all available providers
print([
    provider.__name__
    for provider in g4f.Provider.__providers__
    if provider.working and provider.supports_gpt_4
])

# Execute with a specific provider
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4_turbo,
    provider=g4f.Provider.ChatBase,
    messages=[{"role": "user", "content": f"Какой врач поможет вылечить: ангина. Ответь 1 словом"}],
)
if(response[-1] == "."):
    response = response[0:-1]
    print(response)
