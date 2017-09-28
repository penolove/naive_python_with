""" ref https://blog.gtwang.org/programming/python-with-context-manager-tutorial/"""

class loser:
  def __init__(self, yourname):
      self.yourname = yourname

  def __enter__(self):
      return "Hi, loser: "+self.yourname

  def __exit__(self, type, value, traceback):
      print("Ok loser: "+ self.yourname +" you are free now" )



if __name__=="__main__":
    
    print("start of program")

    # get in with will exec __init__ and __enter__
    with loser("howhow") as f:
        print("Inside with 1")
        print (f)
        print("Inside with 2")
    # out with exec __exit__
    print("end of program")
