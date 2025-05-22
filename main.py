import streamlit as st
import os
import glob
from ast import literal_eval
import subprocess
import sys
import ctypes
import pandas as pd

# Import clara components
from clara.interpreter import getlanginter
from clara.parser import getlangparser
from clara.feedback import Feedback, FeedGen
from clara.feedback_python import PythonFeedback

path = os.getenv("LD_LIBRARY_PATH", "")
build_path = os.getenv("build_path", "")

if "/mount" in path and not (os.path.exists(build_path)) :
    subprocess.run([sys.executable, 'setup.py', 'build_ext', '--inplace'], check=True)

    lib_path = os.path.join(path, 'liblpsolve55.so')
    ctypes.CDLL(lib_path)

# Configure Streamlit page
st.set_page_config(
    page_title="Clara Feedback Analysis",
    page_icon="🔍",
    layout="wide"
)

def load_program(uploaded_file):
    """Helper function to load and parse program from uploaded file"""
    if uploaded_file is None:
        return None, None

    try:
        # Read content of uploaded file
        content = uploaded_file.getvalue().decode("utf-8")

        # Get file extension to determine language
        file_extension = uploaded_file.name.split('.')[-1]

        # Get parser for the language
        parser = getlangparser(file_extension)

        # Parse the code
        model = parser.parse_code(content)
        model.name = uploaded_file.name

        return model, file_extension
    except Exception as e:
        st.error(f"Error loading program: {str(e)}")
        return None, None

def load_correct_programs(cluster_dir, lang):
    """Load correct programs from clusters directory"""
    correct_programs = []
    try:
        for f in glob.glob(os.path.join(cluster_dir, f"*.{lang}")):
            with open(f, 'r', encoding='utf-8') as file:
                parser = getlangparser(lang)
                model = parser.parse_code(file.read())
                model.name = f
                correct_programs.append(model)
    except Exception as e:
        st.error(f"Error loading cluster programs: {str(e)}")
    return correct_programs

def main():
    try:
        st.title("Clara Feedback Analysis")

        # Side Bar
        st.sidebar.subheader("List Problem")
        problem_type = st.sidebar.radio(
            "Select Problem",
            ["problemA", "problemB", "problemC", "problemD", "problemE", "problemF"]
        )

        # Configuration
        verbose = False
        entry_func = problem_type
        timeout = 60

        # Program inputs
        args_input = ""
        ins_input = ""

        # Parse args and ins
        args = None
        ins = None

        if(problem_type == "problemA") :
            st.write("""
                ### SIM Planet X
                Di planet X yang berjarak 10 tahun cahaya dari planet Bumi syarat untuk mendapatkan SIM adalah minimal berumur 10 tahun, fasih berbahasa python, dan nilai tes kecakapan mengemudinya tepat 100.

                ### Input Format
                Input dalam satu baris berupa dua bilangan bulat **Umur** dan **Nilai**, serta boolean **Fasih**.

                ### Output Format
                Output dalam satu baris berupa Boolean **True** jika bisa mendapatkan SIM, atau **False** jika belum bisa.

                ### Constraints
                - 1 ≤ **umur** ≤ 100
                - 0 ≤ **nilai** ≤ 100
            """)
            st.write("### Sample 1")
            data = {
                "Input": ["10 True 100", "8 False 99", "7 True 68"],
                "Output": ["True", "False", "False"]
            }

            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(data)

            st.markdown("""
                <style>
                .full-width-table {
                    width: 100%;
                    text-align: left;
                }

                .full-width-table th {
                    text-align: left;  /* Aligns the header text to the left */
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table without index and make it full width
            st.markdown(df.to_html(index=False, classes="full-width-table"), unsafe_allow_html=True)

            args_input = "[[[10, True, 100]], [[8, False, 99]], [[7, True, 68]], [[10, True, 26]], [[5, True, 100]]]"
            type = "A"
        elif(problem_type == "problemB") :
            st.write("""
                ### Kelipatan Bilangan
                Buatlah program untuk memeriksa apakah bilangan a kelipatan dari bilangan b.

                ### Input Format
                Input dalam satu baris berupa dua bilangan bulat **a** dan **b**.

                ### Output Format
                Output dalam satu baris berupa string **Kelipatan** jika a kelipatan b, dan string **Bukan kelipatan** jika a bukan kelipatan b.

                ### Constraints
                1 ≤ **a**, **b** ≤ 9999
            """)
            st.write("### Samples")
            data = {
                "Input": ["1 2", "2 1", "3 6"],
                "Output": ["Kelipatan", "Bukan kelipatan", "Kelipatan"]
            }

            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(data)

            st.markdown("""
                <style>
                .full-width-table {
                    width: 100%;
                    text-align: left;
                }

                .full-width-table th {
                    text-align: left;  /* Aligns the header text to the left */
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table without index and make it full width
            st.markdown(df.to_html(index=False, classes="full-width-table"), unsafe_allow_html=True)

            args_input = "[[[1, 2]], [[2, 1]], [[3, 6]], [[5, 7]], [[5, 20]]]"
            type = "B"
        elif(problem_type == "problemC") :
            st.write("""
                ### Konversi Waktu
                Buatlah program dalam bahasa Python untuk mengkonversi waktu dalam bilangan bulat dengan satuan jam, menit, dan detik menjadi satuan detik.

                ### Input Format
                Input dalam satu baris berupa tiga bilangan bulat yang menyatakan waktu dalam **jam**, **menit**, dan **detik**.

                ### Output Format
                Output dalam satu baris berupa bilangan bulat yang menyatakan hasil konversi ke detik.

                ### Constraints
                0 ≤ **jam**, **menit**, **detik** ≤ 9999
            """)
            st.write("### Samples")
            data = {
                "Input": ["1 2 3", "1 1 1", "1 2 0"],
                "Output": ["3723", "3661", "3720"]
            }

            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(data)

            st.markdown("""
                <style>
                .full-width-table {
                    width: 100%;
                    text-align: left;
                }

                .full-width-table th {
                    text-align: left;  /* Aligns the header text to the left */
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table without index and make it full width
            st.markdown(df.to_html(index=False, classes="full-width-table"), unsafe_allow_html=True)

            args_input = "[[[1, 2, 3]], [[1, 1, 1]], [[1, 2, 0]], [[0, 0, 1]], [[1, 0, 0]]]"
            type = "C"
        elif(problem_type == "problemD") :
            st.write("""
                ### Tebak Angka
                Adik dan kakak sedang bermain tebak-tebakan bilangan. Keduanya menuliskan sebuah bilangan dari 0 hingga 9 di atas secarik kertas secara rahasia dan kemudian membandingkannya. Adik dinyatakan pemenang **Jika Bilangannya Sama dengan Bilangan Kakak** atau **Selisih Bilangannya 1 atau 5**. Buatlah algoritma untuk menentukan apakah adik pemenang permainan ini.

                ### Input Format
                Input dalam satu baris berupa dua bilangan bulat **adik**(bilangan pertama) dan **kakak**(bilangan kedua).

                ### Output Format
                - Output dalam satu baris berupa boolean **True** atau **False**.
                - **True** berarti adik pemenang permainan ini dan **False** berarti sebaliknya.

                ### Constraints
                0 ≤ **adik**, **kakak** ≤ 9
            """)
            st.write("### Samples")
            data = {
                "Input": ["1 1", "1 2", "1 3"],
                "Output": ["True", "True", "False"]
            }

            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(data)

            st.markdown("""
                <style>
                .full-width-table {
                    width: 100%;
                    text-align: left;
                }

                .full-width-table th {
                    text-align: left;  /* Aligns the header text to the left */
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table without index and make it full width
            st.markdown(df.to_html(index=False, classes="full-width-table"), unsafe_allow_html=True)

            args_input = "[[[1, 1]], [[1, 2]], [[1, 3]], [[2, 6]], [[6, 2]]]"
            type = "D"
        elif(problem_type == "problemE") :
            st.write("""
                ### Penggandaan Digit
                Buatlah program dalam bahasa Python untuk menggandakan digit suatu bilangan. Misalkan, masukan 12, digandakan menjadi 1122.

                ### Input Format
                Input dalam satu baris berupa satu buah bilangan berdigit 2 (digit 1 hingga 9).

                ### Output Format
                Output dalam satu baris berupa bilangan bulat hasil penggandaan.

                ### Constraints
                10 ≤ **bilangan** ≤ 99
            """)
            st.write("### Samples")
            data = {
                "Input": ["12", "32", "28"],
                "Output": ["1122", "3322", "2288"]
            }

            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(data)

            st.markdown("""
                <style>
                .full-width-table {
                    width: 100%;
                    text-align: left;
                }

                .full-width-table th {
                    text-align: left;  /* Aligns the header text to the left */
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table without index and make it full width
            st.markdown(df.to_html(index=False, classes="full-width-table"), unsafe_allow_html=True)

            args_input = "[[[12]], [[32]], [[63]], [[28]], [[72]]]"
            type = "E"
        elif(problem_type == "problemF") :
            st.write("""
                ### Bilangan Konsekutif
                Bilangan konsekutif adalah bilangan yang selisih setiap digit yang bersebelahan adalah satu. Buatlah program dalam bahasa Python untuk menentukan apakah suatu bilangan termasuk konsekutif atau tidak.

                ### Input Format
                Input dalam satu baris berupa sebuah bilangan bulat positif **x**.

                ### Output Format
                Output dalam satu baris berupa sebuah boolean **True** atau **False** yang menyatakan x adalah konsekutif atau tidak.

                ### Constraints
                0 ≤ **x** ≤ 9999
            """)
            st.write("### Samples")
            data = {
                "Input": ["98", "123", "223"],
                "Output": ["True", "True", "False"]
            }

            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(data)

            st.markdown("""
                <style>
                .full-width-table {
                    width: 100%;
                    text-align: left;
                }

                .full-width-table th {
                    text-align: left;  /* Aligns the header text to the left */
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table without index and make it full width
            st.markdown(df.to_html(index=False, classes="full-width-table"), unsafe_allow_html=True)

            args_input = "[[[98]], [[123]], [[223]], [[627]], [[7654]]]"
            type = "F"

        try:
            if args_input.strip():
                args = literal_eval(args_input)
            if ins_input.strip():
                ins = literal_eval(ins_input)
        except Exception as e:
            st.error(f"Error parsing arguments or inputs: {str(e)}")
            return

        st.header("Generate Feedback for '" + problem_type + "'")

        # Upload incorrect program
        incorrect_program = st.file_uploader("Upload program for feedback", key="prog")
        if incorrect_program:
            st.code(incorrect_program.getvalue().decode("utf-8"), language="python")

        # Cluster directory input
        cluster_dir = os.path.join(os.path.dirname(__file__), 'clusters/set1')
        cluster_dir = os.path.join(cluster_dir, type)

        max_cost = 0 #0 means no limit
        clean_strings = False #Clean Strings
        ignore_io = True #Input Output
        ignore_ret = False #Return Value

        if st.button("Generate Feedback", type="primary"):
            if not incorrect_program:
                st.error("Please upload a program for feedback.")
                return

            model, lang = load_program(incorrect_program)
            if not model:
                return

            # Load correct programs from cluster
            correct_programs = load_correct_programs(cluster_dir, lang)
            if not correct_programs:
                st.error(f"No correct programs found in {cluster_dir}")
                return

            interpreter = getlanginter(lang)

            # Set feedback module
            feedmod = PythonFeedback

            feedgen = FeedGen(
                verbose=verbose,
                timeout=timeout,
                allowsuboptimal=True,
                feedmod=feedmod
            )

            with st.spinner("Generating feedback..."):
                try:
                    feedback = feedgen.generate(
                        model, correct_programs, interpreter,
                        ins=ins, args=args,
                        ignoreio=ignore_io,
                        ignoreret=ignore_ret,
                        cleanstrings=clean_strings,
                        entryfnc=entry_func
                    )

                    if feedback.status == Feedback.STATUS_REPAIRED:
                        if max_cost > 0 and feedback.cost > max_cost:
                            st.error(f'Max cost exceeded ({feedback.cost} > {max_cost})')
                        else:
                            if feedback.feedback :
                                st.error("Answer is Incorrect")
                            else :
                                st.success("Answer is Correct")
                    elif feedback.status == Feedback.STATUS_ERROR:
                        st.error(f"Error generating feedback: {feedback.error}")
                    else:
                        st.warning(feedback.statusstr())

                except Exception as e:
                    st.error(f"Error generating feedback: {str(e)}")
                    if verbose:
                        st.exception(e)

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        if verbose:
            st.exception(e)

if __name__ == "__main__":
    main()