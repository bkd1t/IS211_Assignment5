class PrintJob:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
        self.remaining = pages

    def tick(self):
        if self.remaining:
            self.remaining -= 1
        print("Job {}: {} / {} pages remain".format(self.name, self.remaining, self.pages))

    def is_done(self):
        return self.remaining == 0

class JobQueue:
    def __init__(self):
        self.jobs = []

    def enqueue(self, job):
        self.jobs.append(job)

    def dequeue(self):
        return self.jobs.pop(0)

    def is_empty(self):
        return not self.jobs

class Printer:
    def __init__(self, name, job_queue):
        self.name = name
        self.job_queue = job_queue
        self.current_job = None

    def tick(self):
        # make sure we have a job to work on
        if self.current_job is None:
            if self.job_queue.is_empty():
                print("Printer {} is idle".format(self.name))
                return
            else:
                self.current_job = self.job_queue.dequeue()
                print("Printer {} got job {}".format(self.name, self.current_job.name))
        # print!
        print("Printer {} is printing...".format(self.name))
        self.current_job.tick()
        # see if job is finished
        if self.current_job.is_done():
            print("Printer {} finished job {}".format(self.name, self.current_job.name))
            self.current_job = None

    def is_idle(self):
        return self.current_job is None

def main():
    # create job queue and two printers
    jobs = JobQueue()
    p1 = Printer(1, jobs)
    # p2 = Printer(2, jobs)

    # add jobs
    jobs.enqueue(PrintJob(1, 5))
    # jobs.enqueue(PrintJob(2, 7))
    # jobs.enqueue(PrintJob(3, 13))

    # cycle until queue is empty
    tick = 0
    # while not (jobs.is_empty() and p1.is_idle() and p2.is_idle()):
    while not (jobs.is_empty() and p1.is_idle()):
        tick += 1
        print("\n=== Tick {} ===".format(tick))
        p1.tick()
        # p2.tick()

    print("\nAll done! Time for a pint...")

if __name__ == "__main__":
    main()
