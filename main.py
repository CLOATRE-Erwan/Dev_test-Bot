import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if message.content.startswith('!model'):
    await message.channel.send('```python\ndef model(X, theta):\n  return X.dot(theta)```')

  if message.content.startswith('!cost_function'):
    await message.channel.send('```python\ndef cost_function(X, y, theta):\n  m =l(y)\n return 1/(2*m) * np.sum((model(X, theta) - y)**2)```')
    
  if message.content.startswith('!grad'):
    await message.channel.send('```python\ndef cost_function(X, y, theta):\n  m =l(y)\n return 1/(2*m) * np.sum((model(X, theta) - y)**2)```')

  if message.content.startswith('!gradient_descent'):
    await message.channel.send('```python\ndef gradient_descent(X, y, theta, learning_rate, n_iterations):\n for i in range(0, n_iterations):\n  theta = theta - learning_rate * grad(X, y, theta)\n return theta```')

client.run(os.getenv('token'))