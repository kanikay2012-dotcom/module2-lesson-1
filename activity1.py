medical_cause = input("DID YOU HAVE ANY MEDICAL ISSUE? (Y/N:)").strip().upper()
if medical_cause =='y':
    print("You are allowed to take the exam.")
else:
    atten = int(input("Attendence of the sudent:"))
    if atten>75 or atten ==75:
        print("allowed to take the exam.")
    else:
        print("not allowed to tke the exam.")