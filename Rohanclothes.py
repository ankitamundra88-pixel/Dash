Get_Clothing_Advice(temp):
if temp >= 25:
    return "It's hot outside! Wear light and breathable clothing, such as shorts and a t-shirt."
elif temp >= 18:
    return "The weather is mild. You can wear comfortable clothing like jeans and a long-sleeve shirt."
elif temp >= 12:
    return "It's a bit chilly. Consider wearing a light jacket or sweater along with your regular clothes."
elif temp >= 5:
    return "It's cold outside. You should wear a warm coat, scarf, and gloves to stay comfortable."
else:
    return "It's very cold! Make sure to bundle up with a heavy coat, hat, gloves, and a scarf to stay warm."
def main():
    print("=" * 40)
    print("   Rohan's Weather Clothing Advicer")
    print()
    print(" Rohan is tired of his jacket and pullovers.")
    print("Let's check if today's temperature is safe.")
    print("For wearing something light and soft")
    