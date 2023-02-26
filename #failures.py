#failures
while True:
    try:
        x=int(input("please type a number"))
        #value error
        y=int(input("2nd number please"))
        print(x/y)
    except ZeroDivisionError:
        print("0 cannot be applicable for y")
    except ValueError:
        print("please insert a number only ")
    except Exception as mistake:
        print("oops",mistake)

#except (ZeroDivisionError,ValueError): # birleştirilerek yazılabilir.
 #   print("wrong input")
    else:
        print("it is fluent")
        break

#syntax error
#indentation error > girinti hatası
#name error
# 0 division error
