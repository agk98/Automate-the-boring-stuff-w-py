birthdays={'John':'May 12','Alice':'January 20','Hill':'March 21','Mark':'April 1'}
while True:
    print('Enter the Name whose birthday is to be found(Space to exit): ')

    name=input()
    if name==' ':
            break
    if name in birthdays:
        print(birthdays[name])
    else:
        print('name does not exist')

          
