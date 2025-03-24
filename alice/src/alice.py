from utils import *

MY_NAME = 'Alice'

def main():
    config_file = '/home/christian/alice/config/p2p.cfg'
    config = load_config(config_file)

    disp_middle(text='Alice', fontsize=14)

    # Get user input, i.e. secret number
    my_secret = get_number(MY_NAME)
    disp_middle(text=f'My secret number: {my_secret}')

    # Step 1: rolling dialogue
    disp_middle(text=f'Rolling dice...')
    my_rand = roll_dice(MY_NAME)
    disp_middle(text=f'I rolled "{my_rand}"')
    
    # Step 2: Substract own random
    current = subtract_rand(MY_NAME, my_secret, my_rand)
    
    # Step 3: Send to Bob
    print('I am safe to share my random number!')
    send(MY_NAME, 'Bob', config, my_rand)
    disp_middle(text=f'Send {my_rand} to Bob')

    # Step 4: Get Number from Charlie
    print('Now Bob and Charlie are generating randomness')
    print('Have a look at the displays!')
    charlies_rand = receive('Charlie', MY_NAME, config)
    print("I got Charlie's random number!")
    disp_middle(text=f'Got {charlies_rand} from Charlie')

    # Step5: Add Cahrlie's random
    current = add_rand(MY_NAME, my_secret, current ,my_rand, charlies_rand)

    print('Lets do some math with this:')
    print('\n1st subtract my random number')
    print('from my secret number:')
    print(f'{my_secret}-{my_rand}={my_secret-my_rand}')
    print("\n2nd add Charlie's random number:")
    print(f'{my_secret}-{my_rand}+{charlies_rand}={current}')
    disp_two_lines(
        line1='',
        line2=f'Doing some math:',
        line3=f'{my_secret}-{my_rand}+{charlies_rand}={current}'
        )
    
    # Step6: Finally do the calculation
    s1,s2,s3 = share_random_current(config, 0, current)
    disp_middle(text=f'Share "{current}" with both')
    time.sleep(2)
    disp_two_lines(
        line1=f"Alice's Secret: {my_secret}",
        line2=f'Final sum:',
        line3 = f'{s1}+{s2}+{s3}={s1+s2+s3}')
    print(" ----------------------------------------")
    print('Reload the page if you want to rerun!')
    print('Please close the page if you are done!')
    print(" ----------------------------------------")
    time.sleep(60)

if __name__ == "__main__":
    main()
