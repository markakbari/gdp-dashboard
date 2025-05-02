
import streamlit as st
import datetime

# عنوان
st.title("FocusFlow - مدیریت هوشمند زمان و انرژی")

# بخش هدف‌های هفته
st.header("🎯 هدف‌های این هفته")
weekly_goals = st.text_area("اهداف خود را برای این هفته بنویس:", height=100)

# بخش برنامه‌ریزی روزانه
st.header("✅ برنامه امروز")

today = datetime.date.today()
st.subheader(f"تاریخ: {today}")

task1 = st.text_input("اولویت ۱:")
task2 = st.text_input("اولویت ۲:")
task3 = st.text_input("اولویت ۳:")

done1 = st.checkbox("اولویت ۱ انجام شد؟")
done2 = st.checkbox("اولویت ۲ انجام شد؟")
done3 = st.checkbox("اولویت ۳ انجام شد؟")

# بخش پومودورو تایمر ساده (نمایشی)
st.header("⏱️ تایمر تمرکز (Pomodoro)")
st.info("پیشنهاد: ۲۵ دقیقه تمرکز → ۵ دقیقه استراحت")

if st.button("شروع تمرکز ۲۵ دقیقه‌ای"):
    st.success("تایمر شروع شد! (در نسخه نهایی، تایمر واقعی اضافه می‌شود)")

# یادآوری سلامت
st.header("🧘 مراقبت از خود")

sleep = st.slider("چند ساعت خوابیدی دیشب؟", 0, 12, 7)
exercise = st.selectbox("امروز ورزش کردی؟", ["نه هنوز", "بله - کمتر از ۳۰ دقیقه", "بله - بیشتر از ۳۰ دقیقه"])
disconnect = st.checkbox("یک ساعت قبل از خواب از موبایل فاصله گرفتی؟")

# جمع‌بندی
st.header("📊 خلاصه روزانه")

if st.button("ثبت گزارش روز"):
    score = 0
    if done1: score += 1
    if done2: score += 1
    if done3: score += 1
    if sleep >= 7: score += 1
    if exercise != "نه هنوز": score += 1
    if disconnect: score += 1

    st.success(f"امتیاز بهره‌وری امروز: {score}/6")
