# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.fftpack import fft

# # Function to perform weighted Fourier analysis
# def perform_weighted_fourier_analysis(time, signal, amplitude_errors, sampling_rate):
#     # Compute the weights based on amplitude errors
#     weights = 1.0 / amplitude_errors

#     # Apply weights to the signal
#     weighted_signal = signal * weights

#     # Compute the Fast Fourier Transform (FFT) with weighted signal
#     n = len(weighted_signal)
#     frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
#     fft_values = np.fft.fft(weighted_signal)

#     return frequencies, fft_values

# # Function to plot the time series and Fourier analysis results
# def plot_results(time, signal, frequencies, fft_values, sampling_rate):
#     plt.figure(figsize=(12, 6))

#     # Plot the time series
#     plt.subplot(2, 1, 1)
#     plt.plot(time, signal)
#     plt.title('Time Series')
#     plt.xlabel('Time (s)')
#     plt.ylabel('Amplitude')

#     # Plot the Fourier Transform
#     plt.subplot(2, 1, 2)
#     plt.plot(frequencies, np.abs(fft_values))
#     plt.title('Fourier Transform')
#     plt.xlabel('Frequency (Hz)')
#     plt.ylabel('Amplitude')

#     plt.tight_layout()
#     plt.show()

# # Main program
# # Assuming the time series data is in a text file with three columns: time, amplitude, and amplitude_error
# file_path = 'TimeSeries-2459199.6807775-121520UT.txt'
# data = np.loadtxt(file_path,skiprows=1)

# # Extract time, amplitude, and amplitude error columns
# time_series = data[:, 0]
# amplitude_series = data[:, 1]
# amplitude_errors = data[:, 2]

# sampling_rate = 1 / (time_series[1] - time_series[0])

# # Perform weighted Fourier analysis
# frequencies, fft_values = perform_weighted_fourier_analysis(
#     time_series, amplitude_series, amplitude_errors, sampling_rate
# )

# # Plot the results
# plot_results(time_series, amplitude_series, frequencies, fft_values, sampling_rate)


import numpy as np
import matplotlib.pyplot as plt

def read_time_series(file_path):
    data = np.loadtxt(file_path,skiprows=1)
    time = data[:, 0]
    amplitude = data[:, 1]
    amplitude_error = data[:, 2]
    return time, amplitude, amplitude_error

def perform_period_analysis(time, amplitude, amplitude_error):
    n = len(time)
    dt = time[1] - time[0]
    frequency = np.fft.fftfreq(n, dt)
    fft_values = np.fft.fft(amplitude)
    power = np.abs(fft_values) ** 2
    return frequency, power

def plot_periodogram(frequency, power):
    plt.figure(figsize=(10, 6))
    plt.plot(frequency, power)
    #plt.xscale('log')
    plt.title('FFT Periodogram')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.show()

def main():
    # Get input file path from the user
    file_path = input("Enter the path to the time series file: ")

    # Read time series data
    time, amplitude, amplitude_error = read_time_series(file_path)

    # Perform FFT periodogram analysis
    frequency, power = perform_period_analysis(time, amplitude, amplitude_error)

    # Plot the results
    plot_periodogram(frequency, power)

if __name__ == "__main__":
    main()