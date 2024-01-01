import streamlit as st
import pandas as pd
import pickle


with open('rf_model.pkl', 'rb') as model_file:
    loaded_rf_model = pickle.load(model_file)
    

df = pd.read_csv("Extracted Variables.csv")

st.title("Filter Data")
selected_brand = st.selectbox("PC Brand", ["Dell", "Google", "Lenovo", "HP", "Asus", "Acer", "MSI", "Toshiba", 
                                                       "Apple", "Samsung", "Razer", "Mediacom" , "Microsoft", "Xiaomi", "Vero", 
                                                       "Chuwi", "Google", "Fujitsu", "LG", "Huawei"])
selected_os = st.selectbox("Operating System", ["Android", "Windows 10", "Windows 7", "Linux", "Mac OS", "Mac OS X", "Chrome OS", "Windows 10 S", "No OS"])
selected_screen_h = st.slider("Screen Height", min_value=768, max_value=2160)
selected_screen_w = st.slider("Screen Width", min_value=1366, max_value=3840)
selected_cpu_brand = st.selectbox("CPU Brand", ["Intel", "AMD", "Samsung"])
selected_gpu_brand = st.selectbox("GPU Brand", ["Intel", "AMD", "Nvidia", "ARM"])
selected_cpu_freq = st.slider("CPU Frequency (GHz)",min_value=0.9, max_value=3.6, step = 0.1)
selected_weight = st.slider("Weight", min_value=0.7, max_value=4.7, step=0.1)
selected_pc_type = st.selectbox("PC Type", ["Notebook", "2 in 1 Convertible", "Ultrabook", "Netbook", "Gaming", "Workstation"])
selected_inches = st.slider("Inches", min_value=10.1, max_value=18.4)
selected_storage = st.slider("Storage (GB)", min_value=8, max_value=2000)
selected_ram = st.slider("RAM Size (GB)", min_value=2, max_value=64)





inp = pd.DataFrame({
    
    # Brand Names
    "Acer": [1 if selected_brand == "Acer" else 0],
    "Apple": [1 if selected_brand == "Chuwi" else 0],
    "Asus": [1 if selected_brand == "Asus" else 0],
    "Chuwi": [1 if selected_brand == "Chuwi" else 0],
    "Dell": [1 if selected_brand == "Dell" else 0],
    "Fujitsu": [1 if selected_brand == "Fujitsu" else 0],
    "Google": [1 if selected_brand == "Google" else 0],
    "HP": [1 if selected_brand == "HP" else 0],
    "Huawei": [1 if selected_brand == "Huawei" else 0],
    "LG": [1 if selected_brand == "LG" else 0],
    "Lenovo": [1 if selected_brand == "Lenovo" else 0],
    "MSI": [1 if selected_brand == "MSI" else 0],
    "Mediacom": [1 if selected_brand == "Mediacom" else 0],
    "Microsoft": [1 if selected_brand == "Microsoft" else 0],
    "Razer": [1 if selected_brand == "Razer" else 0],
    "Samsung": [1 if selected_brand == "Samsung" else 0],
    "Toshiba": [1 if selected_brand == "Google" else 0],
    "Vero": [1 if selected_brand == "Vero" else 0],
    "Xiaomi": [1 if selected_brand == "Xiaomi" else 0],
    
    
    # OS Names
    "Android": [1 if selected_os == "Android" else 0],
    "Windows 10": [1 if selected_os == "Windows 10" else 0],
    "Windows 10 S": [1 if selected_os == "Windows 10 S" else 0],
    "Windows 7": [1 if selected_os == "Windows 7" else 0],
    "macOS": [1 if selected_os == "Mac OS" else 0],
    "Mac OS X": [1 if selected_os == "Mac OS X" else 0],
    "Linux": [1 if selected_os == "Linux" else 0],
    "Chrome OS": [1 if selected_os == "Chrome OS" else 0],
    "No OS": [1 if selected_os == "No OS" else 0],
    
    # CPU Brands
    "Intel_CPU": [1 if selected_cpu_brand == "Intel" else 0],
    "Samsung_CPU": [1 if selected_cpu_brand == "Samsung" else 0],
    "AMD_CPU": [1 if selected_cpu_brand == "AMD" else 0],
    
    # GPU Brands
    "Intel_GPU": [1 if selected_gpu_brand == "Intel" else 0],
    "Nvidia_GPU": [1 if selected_gpu_brand == "Nvidia" else 0],
    "AMD_GPU": [1 if selected_gpu_brand == "AMD" else 0],
    "ARM_GPU": [1 if selected_gpu_brand == "ARM" else 0],
    
    # PC Types
    "Notebook": [1 if selected_pc_type == "Notebook" else 0],
    "2 in 1 Convertible": [1 if selected_pc_type == "2 in 1 Convertible" else 0],
    "Netebook": [1 if selected_pc_type == "Netebook" else 0],
    "Ultrabook": [1 if selected_pc_type == "Ultrabook" else 0],
    "Gaming": [1 if selected_pc_type == "Gaming" else 0],
    "Workstation": [1 if selected_pc_type == "Workstation" else 0],
    
    # Slider Parameters
    "ScreenHeight": selected_screen_h,
    "ScreenWidth": selected_screen_w,
    "Weight": selected_weight,
    "Ram": selected_ram,
    "Inches": selected_inches,
    "CpuFreq": selected_cpu_freq,
    "Storage": selected_storage
    
    
})

if st.button("Submit"):
    predict = loaded_rf_model.predict(inp)
    st.write("The Predicted price is: ", round(predict[0], 2))