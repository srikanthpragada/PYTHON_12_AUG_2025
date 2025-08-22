
st = "10:20: 34 :A4:50"

total = 0
nums = st.split(":")
#print(nums)

for n in nums:
    total += int(n)

print(total)