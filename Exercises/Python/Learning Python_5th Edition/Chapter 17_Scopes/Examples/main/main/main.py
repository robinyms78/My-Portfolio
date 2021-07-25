from scope_basics import ScopeBasic
from global_statement import GlobalStatement
from scopes_nested_functions import Nested
from nonlocal_statement import NonLocal
from state_retention_options import State
from makeopen import MakeOpen


def main():
    # Python Scope Basics
    scope = ScopeBasic()
    scope.example1()
    scope.example2()
    scope.example3()
    scope.example4()
    scope.example5()
    scope.example6()
    scope.example7()

    # The global Statement
    g = GlobalStatement()
    g.example1()
    g.example2()
    g.example3()
    g.example4()
    g.example5()
    g.example6()

    # Scopes and Nested Functions
    nested = Nested()
    nested.example1()
    nested.example2()
    nested.example3()
    nested.example4()
    nested.example5()
    nested.example6()
    nested.example7()
    nested.example8()
    nested.example9()
    nested.example10()
    nested.example11()

    # The nonlocal Statement in 3.X
    nl = NonLocal()
    nl.example1()
    nl.example2()
    nl.example3()
    nl.example4()
    nl.example5()
    nl.example6()

    # Why nonlocal? State Retention Options
    state = State()
    state.example1()
    state.example2()
    state.example3()
    state.example4()
    state.example5()
    state.example6()

    # Why You Will Care: Customizing Open
    make = MakeOpen()
    make.example1()
    make.example2()


if __name__ == "__main__":
    main()

