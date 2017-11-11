import multi_get
import UserPreferences

if __name__ == "__main__":

# example of using multi_get
    '''
        ids = ["89575","233835","192416"]
        data = multi_get.multi_get(ids)
        print(data.text)
    '''

    duration_start = input("Enter the data you are available from (mm/dd/yyyy): ")
    duration_end = input("Enter the data you are available until (mm/dd/yyyy): ")
    duration = input("Enter the duration in days: ")

    User_P = UserPreferences.UserP(duration_start,duration_end,duration)
    User_P
