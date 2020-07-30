##Ben Sehnert---bps53@drexel.edu---12455911
##CS172
##Professor D. Augenblick

##HW1 socialite class
class Socialite:

    #initializer method
    def __init__(self, first, last, pic, web, desc, uID):
        self._firstName = first
        self._lastName = last
        self._picture = pic
        self._website = web
        self._description = desc
        self._userID = uID

    def __str__(self):
        return "name: {} {}\nPicture: {}\nWebsite: {}\nDescription: {}\nUserID: {}".format(self._firstName, self._lastName, self._picture, self._website, self._description, self._userID)

if __name__ == "__main__":
    test = Socialite('Ben', 'Sehnert', 'https://no.com', 'apricot.com', 'a picture of me eating a grapefruit', 12345)

    print(test.__str__())
    print("\n\n")
    print(test._description)
    print("\n\n")

    test._description = "no frogs allowed in this outhouse!"

    print(test.__str__())