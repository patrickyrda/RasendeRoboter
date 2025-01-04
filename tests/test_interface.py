def test_gui_launch():
    from game.interface import main
    try:
        main()  # Vérifie que l'interface peut se lancer
        assert True
    except Exception as e:
        assert False, f"L'interface a échoué à se lancer : {e}"
