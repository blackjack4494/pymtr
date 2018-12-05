# pymtr
(Pure) Python Implementation of MTR  

focused platform -> linux/ubuntu  
no gui intended -> focus on cmd line

for now use mtr-packet to send probes and get results  
open a pipe (maybe popen) for input/output

implement similar logic of original mtr program  

simple logic/structure
  - main
    - where everything runs together
  - dns
    - get information about hostname (if no ip is given) and/or dns names
  - net
    - basically the core of pymtr
    - makes use of other submodules to process data and generate useful output
  - pipe
    - mtr-packet handler
    - interface between mtr-packet and python mtr processing
    
possible in near future after complete implementation
  - db
    - add database functionality
  - graph(s/ics)
    - graphical output meaning images (jpg, png, etc.) or for web frameworks django, flask etc.


unanswered questions:
  - mpls
  
  
Goal of this implementation is
  - to have a (pure) python port for mtr
  - to get a better understanding of how mtr works (not only for me in particular)
  - trying to simplify current c implementation
  - to maybe enhance functionality (pyplot, ...?)
  - probably the most important one, to have better documentation
