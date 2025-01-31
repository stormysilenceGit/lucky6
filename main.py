# import random
#
#
# def draw_lottery():
#     while True:
#         try:
#             total_numbers = int(input("请输入要抽取的号码总数（6-49）："))
#             if 6 <= total_numbers <= 49:
#                 break
#             else:
#                 print("请输入范围内的数字！")
#         except ValueError:
#             print("请输入有效的数字！")
#
#     available_numbers = list(range(1, 50))  # 1-49 可选号码
#     drawn_numbers = []
#
#     print("\n开始抽取号码...\n")
#     while len(drawn_numbers) < total_numbers:
#         input("按 Enter 键抽取一个号码...")
#         chosen = random.choice(available_numbers)
#         available_numbers.remove(chosen)
#         drawn_numbers.append(chosen)
#         print(f"抽取的号码：{chosen}")
#         print(f"当前已抽取号码：{sorted(drawn_numbers)}\n")
#
#     print(f"本轮最终号码：{sorted(drawn_numbers)}\n")
#
#     restart = input("是否开始新一轮？(y/n)：").strip().lower()
#     if restart == 'y':
#         draw_lottery()
#     else:
#         print("感谢使用，祝你好运！")
#
#
# # 运行程序
# draw_lottery()

import streamlit as st
import random

# 初始化 session_state
if "selected_numbers" not in st.session_state:
    st.session_state.selected_numbers = []
if "available_numbers" not in st.session_state:
    st.session_state.available_numbers = list(range(1, 50))

# 设置网页标题
st.title("📢 香港六合彩选号")

# 让用户选择总共要抽取的号码数（6-49）
total_numbers = st.slider("选择要抽取的号码总数", min_value=6, max_value=49, value=7)

# 按钮：抽取一个号码
if st.button("🎲 抽取一个号码"):
    if len(st.session_state.selected_numbers) < total_numbers:
        chosen = random.choice(st.session_state.available_numbers)
        st.session_state.available_numbers.remove(chosen)
        st.session_state.selected_numbers.append(chosen)
        st.success(f"🎉 你抽取的号码：{chosen}")
    else:
        st.warning("✅ 已经抽取完所有号码！")

# 显示已经抽取的号码
st.markdown("### 📌 已抽取的号码：")
st.write(sorted(st.session_state.selected_numbers))

# 按钮：重新开始
if st.button("🔄 重新开始"):
    st.session_state.selected_numbers = []
    st.session_state.available_numbers = list(range(1, 50))
    st.info("♻️ 已重置，可以重新选号！")

# 版权信息
st.markdown("---")
st.markdown("🎯 **网页版六合彩选号** - 由 L 提供")
