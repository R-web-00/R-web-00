import os
import multiprocessing

def child_process(write_fd):
    message = "Hello from child process!"
    os.write(write_fd, message.encode())
    os.close(write_fd)

def parent_process():
    pipe_read, pipe_write = os.pipe()

    process = multiprocessing.Process(target=child_process, args=(pipe_write,))
    process.start()

    os.close(pipe_write)

    message = os.read(pipe_read, 1024).decode()
    print(f"Parent received: {message}")

    os.close(pipe_read)
    process.join()

if __name__ == "__main__":
    multiprocessing.set_start_method('fork')  # <-- Add this line on macOS
    parent_process()

# Conclusion:
# The parent and child processes communicate effectively using an os.pipe() mechanism, 
# which creates a unidirectional communication channel.
# The child writes a message to the write end of the pipe, which the parent reads 
# from the read end. Proper closing of unused pipe ends ensures no deadlocks and smooth data transmission.
