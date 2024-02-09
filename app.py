import streamlit as st
import pandas as pd

# Load your clustered products DataFrame
df = pd.read_csv('clustered_products.csv')  # Ensure this path is correct

# Streamlit app
def main():
    st.title('Clustered Products')

    # Dropdown to select cluster
    cluster_options = sorted(df['clusters'].unique())
    selected_cluster = st.selectbox('Select a Cluster', cluster_options)

    # Filter DataFrame based on selected cluster
    filtered_df = df[df['clusters'] == selected_cluster].head(300)  # Assuming you want to limit to 300 rows

    # Display products for the selected cluster in horizontal tiles
    st.subheader(f'Products for Cluster {selected_cluster}')
    
    # Set the number of columns for the layout
    num_of_columns = 3
    cols = st.columns(num_of_columns)
    
    # Display each product in a column
    for index, row in filtered_df.iterrows():
        # Calculate the column index
        col_index = index % num_of_columns
        
        # Display the product image and limited description in the respective column
        with cols[col_index]:
            st.image(row['imgUrl'], width=150)  # Set the width as desired
            # Create an expander to show the full description
            with st.expander("See description"):
                st.write(row['description'])

if __name__ == '__main__':
    main()