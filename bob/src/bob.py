from utils import *

MY_NAME = 'Bob'

def main():
    config_file = '/home/christian/bob/config/p2p.cfg'
    config = load_config(config_file)

    disp_middle(text='Bob', fontsize=14)

    # Get user input, i.e. secret number
    my_secret = get_number(MY_NAME)
    time.sleep(4)
    disp_middle(text=f'My secret number: {my_secret}')

    # Step 1: Get Number from Alice
    alices_rand = receive('Alice', MY_NAME, config)
    disp_middle(text=f'Got {alices_rand} from Alice')
   
    # Step 2 roll dice: 
    disp_middle(text=f'Rolling dice...')
    my_rand = roll_dice(MY_NAME)
    disp_middle(text=f'I rolled "{my_rand}"')

    # Step 3: Substract own random
    current = subtract_rand(MY_NAME, my_secret, my_rand)

    # Step 4: Add Alice's random
    current = add_rand(MY_NAME, my_secret, current, my_rand, alices_rand)

    # Step 5: Send to Charlie
    print('I am safe to share my random number!')
    send(MY_NAME, 'Charlie', config, my_rand)
    disp_middle(text=f'Send {my_rand} to Charlie')
    disp_two_lines(
        line1='',
        line2=f'Doing some math:',
        line3=f'{my_secret}-{my_rand}+{alices_rand}={current}'
        )    

    # Step6: Finally do the calculation
    s1,s2,s3=share_random_current(config, 1, current)
    disp_middle(text=f'Share "{current}" with both')
    time.sleep(5)
    disp_two_lines(
        line1=f"Bob's Secret: {my_secret}",
        line2=f'Final sum:',
        line3 = f'{s2}+{s1}+{s3}={s1+s2+s3}')
    time.sleep(10)
    disp_middle(text='Bob', fontsize=14)
    
if __name__ == "__main__":
    main()
