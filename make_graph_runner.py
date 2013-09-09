from make_graph_job import MRMakeGraph
import time
args = [
    # "-r", "local", "data/", "-o", "output" 
    "-r", "emr",
    #"--emr-job-flow-id=j-2CE25PQL2IHP5",
    #"s3://frames.datawi.re/bafindealings/notice/", 
    "s3://json.twindle.pudo.org/test/", 
    #"data/raw_345130153850064900.json",
    # "-c", "../mrjob.yml",
    "--no-output", "-o", "s3://emr.pudo.org/output-" + str(int(time.time()))
]
job = MRMakeGraph(args=args)
job.run_job()
