import federatedsecure.client
import time
import random
import configparser
from display.drive import SSD1305

from PIL import Image,ImageDraw,ImageFont

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def get_number(may_name):
    secret_number = int(input("Enter a random number between 1 and 9: "))
    print(f'My super secret number is "{secret_number}"')
    time.sleep(1)
    return secret_number

def roll_dice(may_name):
    print('We start with generating a random number')
    _wait_for_enter('Press "y" to roll the dice')
    dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
    for _ in range(10):
        face = random.choice(list(dice_faces.values()))
        print(f"Rolling... {face} ", end="\r", flush=True)
        time.sleep(0.2)
    rand = random.randint(1, 6)
    print(f"I rolled: a {rand}")
    return rand

def subtract_rand(may_name, secret, rand):
    current = secret - rand
    time.sleep(1)
    return current

def add_rand(my_name, secret, current, rand1, rand2):
    current += rand2
    time.sleep(1)
    time.sleep(1)
    return current

def _wait_for_enter(prompt):
    print(prompt, flush=True)
    while input().strip() != "y":
        pass

def _setup_network(parties, myself, config):
    nodes = [config[p]['addr'] for p in parties]
    uuid = config['UUID']['uuid1'] if len(parties) == 2 else config['UUID']['uuid2']
    return {
        'nodes': nodes,
        'uuid': uuid,
        'myself': myself
        }

def _send_number(parties, myself, config, number):
    network = _setup_network(parties, myself, config)
    api = federatedsecure.client.Api(network['nodes'][myself])
    microservice = api.create(protocol='Simon')
    microservice.compute(microprotocol="ShareSecret", data=number, network=network)

def _receive_number(parties, myself, config, number='NaN'):
    network = _setup_network(parties, myself, config)
    api = federatedsecure.client.Api(network['nodes'][myself])
    microservice = api.create(protocol='Simon')
    result = microservice.compute(microprotocol="ShareSecret", data=number, network=network)
    return api.download(result)['secrets']

def receive(sender, receiver, config, number='NaN'):
    print(f'Waiting for random number from {sender}..')
    share = _receive_number([sender, receiver], 1, config, number)[0]
    time.sleep(1)
    print(f'Received {share} from {sender}')
    time.sleep(1)
    return(share)

def send(sender, receiver, config, number):
    _wait_for_enter(f'Press "y" to send your random number to {receiver}')
    print(f'Sending random number to {receiver}')
    _send_number([sender, receiver], 0, config, number)
    return

def share_random_current(config, my_index, current):
    print('Now we are safe to share our random current')
    _wait_for_enter('Press "y" to share your random current')
    print('Sharing the random current')
    result = _receive_number(['Alice', 'Bob', 'Charlie'], my_index, config, current)
    s1 = result[0]
    s2 = result[1]
    s3 = result[2]
    print('I got all random currents:')
    print(f'From Charlie I got:{s3}.')
    print(f'From Bob I got {s2}.')
    print(f'So the final sum is: {s1}+{s2}+{s3}={s1+s2+s3}')
    return s1,s2,s3

####
DISP = SSD1305.SSD1305()
DISP.Init()
DISP.clear()  # Clear display
width = DISP.width
height = DISP.height
image = Image.new('1', (width, height))  # Create a blank image
DRAW = ImageDraw.Draw(image)  # Get drawing object

def get_font(size):
    return ImageFont.truetype('/home/christian/alice/src/display/04B_08__.TTF', size)

def disp_middle(text, fontsize=8):
    FONT = get_font(fontsize)
    bbox = DRAW.textbbox((0, 0), text, font=FONT)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    DRAW.rectangle((0, 0, width, height), outline=0, fill=0)  # Clear screen
    DRAW.text((x, y), text, font=FONT, fill=255)
    DISP.getbuffer(image)
    DISP.ShowImage()

def disp_two_lines(line1, line2, line3, fontsize=8):
    FONT = get_font(fontsize)
    
    # Calculate the width and height of both lines
    bbox2 = DRAW.textbbox((0, 0), line2, font=FONT)
    bbox3 = DRAW.textbbox((0, 0), line3, font=FONT)
    
    text_width2 = bbox2[2] - bbox2[0]
    text_height2 = bbox2[3] - bbox2[1]
    
    text_width3 = bbox3[2] - bbox3[0]
    text_height3 = bbox3[3] - bbox3[1]

    y1 = 0
    # Calculate horizontal position (centered horizontally)
    x2 = (width - text_width2) // 3
    x3 = (width - text_width3) // 3

    # Clear the display
    DRAW.rectangle((0, 0, width, height), outline=0, fill=0)
    
    DRAW.text((0, y1), line1, font=FONT, fill=255)
    DRAW.text((x2, y1+16), line2, font=FONT, fill=255)
    DRAW.text((x3, y1+24), line3, font=FONT, fill=255)

    # Update the display
    DISP.getbuffer(image)
    DISP.ShowImage()
