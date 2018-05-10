label adviserchat:
    $ datecounter += 1
    menu :
        "Who should I go see?"

        "Mirna" if gonetothevillage_flag == False:
            call mirnadate from _call_mirnadate
        "Leo":
            call leodate from _call_leodate
        "Cassandra":
            call cassandradate from _call_cassandradate
        "Alistair":
            call alistairdate from _call_alistairdate
    return
