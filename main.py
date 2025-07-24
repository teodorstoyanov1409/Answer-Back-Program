import request_handler




def analyze_request(user_input):
   user_input = user_input.lower().strip()


   request_patterns = {
       'schedule': {
           'keywords': ['разписание', 'schedule', 'график', 'часове', 'кога', 'класове'],
           'function': request_handler.handle_schedule_request
       },
       'contact': {
           'keywords': ['треньор', 'coach', 'контакт', 'телефон', 'номер', 'връзка'],
           'function': request_handler.handle_coach_contact
       },
       'payment': {
           'keywords': ['цена', 'такса', 'пари', 'плащане', 'колко', 'цени', 'payment', 'cost'],
           'function': request_handler.handle_payment_info
       },
       'facilities': {
           'keywords': ['съоръжения', 'басейн', 'зала', 'facilities', 'services', 'какво има'],
           'function': request_handler.handle_facility_info
       },
       'membership': {
           'keywords': ['членство', 'member', 'предимства', 'benefits', 'какво получавам'],
           'function': request_handler.handle_membership_benefits
       }
   }


   for request_type, data in request_patterns.items():
       for keyword in data['keywords']:
           if keyword in user_input:
               return data['function']()


   return """
   ❓ Съжалявам, не разбирам заявката ви.


   Можете да питате за:
   • Разписание на занятията
   • Контакти на треньори
   • Цени и такси
   • Съоръжения и услуги
   • Предимства на членството


   Опитайте отново с една от тези теми!
   """




def main():
   print("🏊‍♀️ Добре дошли в спортния център!")
   print("=" * 50)
   print("Как мога да ви помогна днес?")
   print("(Напишете 'изход' за излизане)")
   print("-" * 50)


   while True:
       try:
           user_request = input("\n>>> ").strip()


           if user_request.lower() in ['изход', 'exit', 'quit', 'off']:
               print("\n👋 Благодарим ви! До скоро виждане!")
               break


           if not user_request:
               print("Моля, въведете вашата заявка.")
               continue


           response = analyze_request(user_request)
           print(response)


       except KeyboardInterrupt:
           print("\n\n👋 Програмата беше прекратена. До скоро виждане!")
           break
       except Exception as e:
           print(f"\n❌ Възникна грешка: {e}")
           print("Моля, опитайте отново.")




if __name__ == "__main__":
   main()

