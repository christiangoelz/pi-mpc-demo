from utils import *

MY_NAME = 'Charlie'

def main():
    config_file = '/home/christian/charlie/config/p2p.cfg'
    config = load_config(config_file)

    disp_middle(text='Charlie', fontsize=14)
    time.sleep(4)
    # Get user input, i.e. secret number
    my_secret = get_number(MY_NAME)
    disp_middle(text=f'My secret number: {my_secret}')

    # Step 1: Get Number from Bob
    bobs_rand = receive('Bob', MY_NAME, config)
    disp_middle(text=f'Got {bobs_rand} from Bob')
    
    # Step 2 roll dice: 
    disp_middle(text=f'Rolling dice...')
    my_rand = roll_dice(MY_NAME)
    disp_middle(text=f'I rolled "{my_rand}"')

    # Step 3: Substract own random
    current = subtract_rand(MY_NAME, my_secret, my_rand)

    # Step 4: Add Bobs's random
    current = add_rand(MY_NAME, my_secret, current, my_rand, bobs_rand)

    # Step 5: Send to Alice
    print('I am safe to share my random number!')
    send(MY_NAME, 'Alice', config, my_rand)
    disp_middle(text=f'Send {my_rand} to Alice')
    disp_two_lines(
        line1='',
        line2=f'Doing some math:',
        line3=f'{my_secret}-{my_rand}+{bobs_rand}={current}'
        )       

    # Step6: Finally do the calculation
    s1,s2,s3 = share_random_current(config, 2, current)
    disp_middle(text=f'Share "{current}" with both')
    time.sleep(5)
    disp_two_lines(
        line1=f"Charlie's Secret: {my_secret}",
        line2=f'Final sum:',
        line3 = f'{s3}+{s2}+{s1}={s1+s2+s3}')
    time.sleep(10)
    disp_middle(text='Charlie', fontsize=14)

if __name__ == "__main__":
    main()
