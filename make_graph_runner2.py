from make_graph_job import MRMakeGraph
args = [
    # "-r", "local", "data/", "-o", "output" 
    "-r", "hadoop", "data/", 
    # "-c", "../mrjob.yml",
    "--no-output", "-o", "s3://emr.pudo.org/output"
]
job = MRMakeGraph(args=args)
job.run_job()

