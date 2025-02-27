
# QuLab Loan Amortization Visualizer

## Description

This Streamlit application, **QuLab Loan Amortization Visualizer**, is an interactive tool designed to help you understand the concept of loan amortization. By visualizing how your loan payments are distributed between principal and interest over time, it provides a clear picture of your loan repayment journey.

**Key Features:**

- **Interactive Loan Parameter Input:** Easily adjust loan parameters such as:
    - **Principal Amount:** The initial amount borrowed.
    - **Annual Interest Rate:** The yearly interest rate on the loan.
    - **Loan Term (Years):** The duration of the loan in years.
- **Detailed Amortization Schedule:** View a comprehensive table outlining each monthly payment, including:
    - Monthly Payment Amount
    - Principal Payment
    - Interest Payment
    - Remaining Loan Balance
    - Cumulative Principal Paid
    - Cumulative Interest Paid
- **Visual Payment Breakdown:** A dynamic line chart illustrating how the monthly payment is split between principal and interest throughout the loan term. Observe the shift from higher interest payments to higher principal payments over time, which is the essence of amortization.
- **Cumulative Payment Analysis:** A bar chart visualizing the cumulative principal and interest paid over the loan's lifetime. This highlights the total cost of borrowing and how your payments contribute to reducing the principal balance.
- **Key Loan Summary Metrics:** Instantly see essential loan summary figures, including:
    - Monthly Payment Amount
    - Total Principal Paid over the loan term
    - Total Interest Paid over the loan term

**Educational Value:**

This application serves as an excellent educational resource for:

- Understanding the mechanics of loan amortization.
- Exploring the impact of different loan parameters on the repayment schedule.
- Gaining insights into the long-term costs associated with borrowing money.

Whether you're planning to take out a loan, are currently paying one off, or are simply curious about personal finance, the QuLab Loan Amortization Visualizer offers a user-friendly and informative experience.

## Installation

To run this Streamlit application, you need to have Python installed on your system along with the required Python packages. Follow these steps to set up the application:

1.  **Prerequisites:** Ensure you have Python installed on your machine. You can download Python from [https://www.python.org/](https://www.python.org/). It is recommended to use Python 3.8 or higher.

2.  **Create a virtual environment (Recommended):**  It's good practice to create a virtual environment to isolate project dependencies. Open your terminal or command prompt and navigate to the directory where you plan to save the application files. Then, run the following commands:

    ```bash
    python -m venv venv  # Create a virtual environment named 'venv'
    ```

    -   **Activate the virtual environment:**
        -   **On macOS/Linux:**
            ```bash
            source venv/bin/activate
            ```
        -   **On Windows:**
            ```bash
            venv\Scripts\activate
            ```

3.  **Install required Python packages:**  Use `pip`, the Python package installer, to install the necessary libraries.

    ```bash
    pip install streamlit pandas numpy
    ```

    This command will install Streamlit, pandas for data manipulation, and numpy for numerical operations, which are required to run this application.

4.  **Save the application code:** Copy the provided Python code (starting with `import streamlit as st` and ending with the copyright and caption lines) and save it as a Python file, for example, `loan_amortization_app.py`, in the same directory where you initialized your virtual environment (or any directory if you skipped the virtual environment step).

## Usage

1.  **Navigate to the application directory:** In your terminal or command prompt, navigate to the directory where you saved the `loan_amortization_app.py` file. If you created and activated a virtual environment, ensure it is still active.

2.  **Run the Streamlit application:** Execute the following command in your terminal:

    ```bash
    streamlit run loan_amortization_app.py
    ```

    Replace `loan_amortization_app.py` with the actual name of your Python file if you saved it with a different name.

3.  **Access the application in your browser:** Streamlit will automatically launch the application in your default web browser. You will typically see a message in your terminal indicating the local URL where the app is running (usually `http://localhost:8501` or `http://127.0.0.1:8501`). If it doesn't open automatically, copy and paste this URL into your browser's address bar and press Enter.

4.  **Interact with the Loan Amortization Visualizer:**

    -   **Loan Parameters Sidebar:** On the left sidebar, you will find input controls to customize your loan scenario:
        -   **Principal Amount:** Enter the desired loan principal using the number input.
        -   **Annual Interest Rate (%):** Use the slider to select the annual interest rate percentage.
        -   **Loan Term (Years):** Use the slider to choose the loan term in years.

    -   **View Results:** As you adjust the loan parameters in the sidebar, the application will dynamically update the following on the main page:
        -   **Amortization Schedule:** A table displaying the month-by-month breakdown of your loan payments.
        -   **Payment Breakdown Over Time Chart:** A line chart visualizing the principal and interest portions of each payment over the loan term.
        -   **Cumulative Payments Chart:** A bar chart showing the cumulative principal and interest paid.
        -   **Key Loan Summary:** Metrics displaying the calculated monthly payment, total principal paid, and total interest paid for the specified loan parameters.

Experiment with different loan amounts, interest rates, and loan terms to observe how they impact the amortization schedule and the overall cost of the loan.

## Credits

This application is developed by **QuantUniversity** for educational and demonstration purposes.

-   **QuantUniversity Website:** [https://www.quantuniversity.com/](https://www.quantuniversity.com/)
-   **Logo:** The Streamlit application uses the QuantUniversity logo, which is displayed in the sidebar and is sourced from [https://www.quantuniversity.com/assets/img/logo5.jpg](https://www.quantuniversity.com/assets/img/logo5.jpg).

## License

© 2025 QuantUniversity. All Rights Reserved.

This application is provided for educational use and illustration only. For any use beyond personal learning, or for commercial purposes, please contact QuantUniversity for legal documentation and permissions. Reproduction, redistribution, or commercial use of this application without prior written consent from QuantUniversity is prohibited.

---
