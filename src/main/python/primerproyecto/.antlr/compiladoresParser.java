// Generated from /home/fabri/Escritorio/dhs/proyecto/primerproyecto/src/main/python/primerproyecto/compiladores.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class compiladoresParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PA=1, PC=2, LLA=3, LLC=4, PYC=5, PUNTO=6, COMA=7, SUMA=8, RESTA=9, MULT=10, 
		DIV=11, MOD=12, ASIG=13, AND=14, OR=15, MENOR=16, MAYOR=17, IGUAL=18, 
		MENORIG=19, MAYORIG=20, DIF=21, NUMERO=22, INT=23, DOUBLE=24, LONG=25, 
		CHAR=26, STRING=27, VOID=28, WHILE=29, FOR=30, IF=31, ELSE=32, RETURN=33, 
		DO=34, ID=35, ENTERO=36, DECIMAL=37, WS=38;
	public static final int
		RULE_comparadores = 0, RULE_tdato = 1, RULE_tfuncion = 2, RULE_programa = 3, 
		RULE_funcion = 4, RULE_parametros = 5, RULE_parametrosp = 6, RULE_usofuncion = 7, 
		RULE_argumentos = 8, RULE_argumentosp = 9, RULE_instrucciones = 10, RULE_instruccion = 11, 
		RULE_bloque = 12, RULE_icontrol = 13, RULE_declaracion = 14, RULE_asignacion = 15, 
		RULE_return = 16, RULE_opal = 17, RULE_lor = 18, RULE_lorp = 19, RULE_land = 20, 
		RULE_landp = 21, RULE_comp = 22, RULE_exp = 23, RULE_e = 24, RULE_term = 25, 
		RULE_t = 26, RULE_factor = 27, RULE_iwhile = 28, RULE_iif = 29, RULE_ifor = 30, 
		RULE_init = 31, RULE_cond = 32, RULE_iter = 33;
	private static String[] makeRuleNames() {
		return new String[] {
			"comparadores", "tdato", "tfuncion", "programa", "funcion", "parametros", 
			"parametrosp", "usofuncion", "argumentos", "argumentosp", "instrucciones", 
			"instruccion", "bloque", "icontrol", "declaracion", "asignacion", "return", 
			"opal", "lor", "lorp", "land", "landp", "comp", "exp", "e", "term", "t", 
			"factor", "iwhile", "iif", "ifor", "init", "cond", "iter"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "';'", "'.'", "','", "'+'", "'-'", 
			"'*'", "'/'", "'%'", "'='", "'&&'", "'||'", "'<'", "'>'", "'=='", "'<='", 
			"'>='", "'=!'", null, "'int'", "'double'", "'long'", "'char'", "'string'", 
			"'void'", "'while'", "'for'", "'if'", "'else'", "'return'", "'do'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PA", "PC", "LLA", "LLC", "PYC", "PUNTO", "COMA", "SUMA", "RESTA", 
			"MULT", "DIV", "MOD", "ASIG", "AND", "OR", "MENOR", "MAYOR", "IGUAL", 
			"MENORIG", "MAYORIG", "DIF", "NUMERO", "INT", "DOUBLE", "LONG", "CHAR", 
			"STRING", "VOID", "WHILE", "FOR", "IF", "ELSE", "RETURN", "DO", "ID", 
			"ENTERO", "DECIMAL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "compiladores.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public compiladoresParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparadoresContext extends ParserRuleContext {
		public TerminalNode MENOR() { return getToken(compiladoresParser.MENOR, 0); }
		public TerminalNode MAYOR() { return getToken(compiladoresParser.MAYOR, 0); }
		public TerminalNode IGUAL() { return getToken(compiladoresParser.IGUAL, 0); }
		public TerminalNode MENORIG() { return getToken(compiladoresParser.MENORIG, 0); }
		public TerminalNode MAYORIG() { return getToken(compiladoresParser.MAYORIG, 0); }
		public TerminalNode DIF() { return getToken(compiladoresParser.DIF, 0); }
		public ComparadoresContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparadores; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterComparadores(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitComparadores(this);
		}
	}

	public final ComparadoresContext comparadores() throws RecognitionException {
		ComparadoresContext _localctx = new ComparadoresContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_comparadores);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4128768L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TdatoContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(compiladoresParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladoresParser.DOUBLE, 0); }
		public TerminalNode CHAR() { return getToken(compiladoresParser.CHAR, 0); }
		public TdatoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tdato; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTdato(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTdato(this);
		}
	}

	public final TdatoContext tdato() throws RecognitionException {
		TdatoContext _localctx = new TdatoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_tdato);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 92274688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TfuncionContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(compiladoresParser.INT, 0); }
		public TerminalNode DOUBLE() { return getToken(compiladoresParser.DOUBLE, 0); }
		public TerminalNode CHAR() { return getToken(compiladoresParser.CHAR, 0); }
		public TerminalNode VOID() { return getToken(compiladoresParser.VOID, 0); }
		public TfuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tfuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTfuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTfuncion(this);
		}
	}

	public final TfuncionContext tfuncion() throws RecognitionException {
		TfuncionContext _localctx = new TfuncionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_tfuncion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 360710144L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(compiladoresParser.EOF, 0); }
		public List<DeclaracionContext> declaracion() {
			return getRuleContexts(DeclaracionContext.class);
		}
		public DeclaracionContext declaracion(int i) {
			return getRuleContext(DeclaracionContext.class,i);
		}
		public List<FuncionContext> funcion() {
			return getRuleContexts(FuncionContext.class);
		}
		public FuncionContext funcion(int i) {
			return getRuleContext(FuncionContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_programa);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(74);
					declaracion();
					}
					} 
				}
				setState(79);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 360710144L) != 0)) {
				{
				{
				setState(80);
				funcion();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(86);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncionContext extends ParserRuleContext {
		public TfuncionContext tfuncion() {
			return getRuleContext(TfuncionContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public FuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFuncion(this);
		}
	}

	public final FuncionContext funcion() throws RecognitionException {
		FuncionContext _localctx = new FuncionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			tfuncion();
			setState(89);
			match(ID);
			setState(90);
			match(PA);
			setState(91);
			parametros();
			setState(92);
			match(PC);
			setState(93);
			bloque();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrosContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public ParametrospContext parametrosp() {
			return getRuleContext(ParametrospContext.class,0);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterParametros(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitParametros(this);
		}
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_parametros);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case DOUBLE:
			case CHAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				tdato();
				setState(96);
				match(ID);
				setState(97);
				parametrosp();
				}
				break;
			case PC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParametrospContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public ParametrospContext parametrosp() {
			return getRuleContext(ParametrospContext.class,0);
		}
		public ParametrospContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametrosp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterParametrosp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitParametrosp(this);
		}
	}

	public final ParametrospContext parametrosp() throws RecognitionException {
		ParametrospContext _localctx = new ParametrospContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_parametrosp);
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				match(COMA);
				setState(103);
				parametros();
				setState(104);
				parametrosp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UsofuncionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public UsofuncionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_usofuncion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterUsofuncion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitUsofuncion(this);
		}
	}

	public final UsofuncionContext usofuncion() throws RecognitionException {
		UsofuncionContext _localctx = new UsofuncionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_usofuncion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(ID);
			setState(110);
			match(PA);
			{
			setState(111);
			argumentos();
			}
			setState(112);
			match(PC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentosContext extends ParserRuleContext {
		public ArgumentospContext argumentosp() {
			return getRuleContext(ArgumentospContext.class,0);
		}
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public ArgumentosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentos; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterArgumentos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitArgumentos(this);
		}
	}

	public final ArgumentosContext argumentos() throws RecognitionException {
		ArgumentosContext _localctx = new ArgumentosContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_argumentos);
		try {
			setState(118);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case NUMERO:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(114);
				opal();
				}
				setState(115);
				argumentosp();
				}
				break;
			case PC:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentospContext extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(compiladoresParser.COMA, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public ArgumentospContext argumentosp() {
			return getRuleContext(ArgumentospContext.class,0);
		}
		public ArgumentospContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentosp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterArgumentosp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitArgumentosp(this);
		}
	}

	public final ArgumentospContext argumentosp() throws RecognitionException {
		ArgumentospContext _localctx = new ArgumentospContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_argumentosp);
		try {
			setState(125);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				match(COMA);
				setState(121);
				argumentos();
				setState(122);
				argumentosp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionesContext extends ParserRuleContext {
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instrucciones; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInstrucciones(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInstrucciones(this);
		}
	}

	public final InstruccionesContext instrucciones() throws RecognitionException {
		InstruccionesContext _localctx = new InstruccionesContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_instrucciones);
		try {
			setState(131);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PA:
			case LLA:
			case PYC:
			case NUMERO:
			case INT:
			case DOUBLE:
			case CHAR:
			case WHILE:
			case FOR:
			case IF:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				instruccion();
				setState(128);
				instrucciones();
				}
				break;
			case LLC:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public IcontrolContext icontrol() {
			return getRuleContext(IcontrolContext.class,0);
		}
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public UsofuncionContext usofuncion() {
			return getRuleContext(UsofuncionContext.class,0);
		}
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public ReturnContext return_() {
			return getRuleContext(ReturnContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInstruccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInstruccion(this);
		}
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_instruccion);
		try {
			setState(141);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				declaracion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				icontrol();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(135);
				bloque();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(136);
				asignacion();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(137);
				usofuncion();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(138);
				opal();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(139);
				return_();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(140);
				match(PYC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BloqueContext extends ParserRuleContext {
		public TerminalNode LLA() { return getToken(compiladoresParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladoresParser.LLC, 0); }
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_bloque);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(LLA);
			setState(144);
			instrucciones();
			setState(145);
			match(LLC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IcontrolContext extends ParserRuleContext {
		public IwhileContext iwhile() {
			return getRuleContext(IwhileContext.class,0);
		}
		public IforContext ifor() {
			return getRuleContext(IforContext.class,0);
		}
		public IifContext iif() {
			return getRuleContext(IifContext.class,0);
		}
		public IcontrolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_icontrol; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIcontrol(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIcontrol(this);
		}
	}

	public final IcontrolContext icontrol() throws RecognitionException {
		IcontrolContext _localctx = new IcontrolContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_icontrol);
		try {
			setState(150);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WHILE:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				iwhile();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				ifor();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(149);
				iif();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterDeclaracion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitDeclaracion(this);
		}
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_declaracion);
		try {
			setState(162);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(152);
				tdato();
				setState(153);
				match(ID);
				setState(154);
				match(PYC);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				tdato();
				setState(157);
				match(ID);
				setState(158);
				match(ASIG);
				setState(159);
				opal();
				setState(160);
				match(PYC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(ID);
			setState(165);
			match(ASIG);
			setState(166);
			opal();
			setState(167);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(compiladoresParser.RETURN, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TerminalNode PYC() { return getToken(compiladoresParser.PYC, 0); }
		public ReturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterReturn(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitReturn(this);
		}
	}

	public final ReturnContext return_() throws RecognitionException {
		ReturnContext _localctx = new ReturnContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(RETURN);
			setState(170);
			opal();
			setState(171);
			match(PYC);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OpalContext extends ParserRuleContext {
		public LorContext lor() {
			return getRuleContext(LorContext.class,0);
		}
		public OpalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterOpal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitOpal(this);
		}
	}

	public final OpalContext opal() throws RecognitionException {
		OpalContext _localctx = new OpalContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_opal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			lor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LorContext extends ParserRuleContext {
		public LandContext land() {
			return getRuleContext(LandContext.class,0);
		}
		public LorpContext lorp() {
			return getRuleContext(LorpContext.class,0);
		}
		public LorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLor(this);
		}
	}

	public final LorContext lor() throws RecognitionException {
		LorContext _localctx = new LorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_lor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			land();
			setState(176);
			lorp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LorpContext extends ParserRuleContext {
		public TerminalNode OR() { return getToken(compiladoresParser.OR, 0); }
		public LandContext land() {
			return getRuleContext(LandContext.class,0);
		}
		public LorpContext lorp() {
			return getRuleContext(LorpContext.class,0);
		}
		public LorpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lorp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLorp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLorp(this);
		}
	}

	public final LorpContext lorp() throws RecognitionException {
		LorpContext _localctx = new LorpContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_lorp);
		try {
			setState(183);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OR:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				match(OR);
				setState(179);
				land();
				setState(180);
				lorp();
				}
				break;
			case PA:
			case PC:
			case LLA:
			case LLC:
			case PYC:
			case COMA:
			case NUMERO:
			case INT:
			case DOUBLE:
			case CHAR:
			case WHILE:
			case FOR:
			case IF:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LandContext extends ParserRuleContext {
		public CompContext comp() {
			return getRuleContext(CompContext.class,0);
		}
		public LandpContext landp() {
			return getRuleContext(LandpContext.class,0);
		}
		public LandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_land; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLand(this);
		}
	}

	public final LandContext land() throws RecognitionException {
		LandContext _localctx = new LandContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_land);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			comp();
			setState(186);
			landp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LandpContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(compiladoresParser.AND, 0); }
		public CompContext comp() {
			return getRuleContext(CompContext.class,0);
		}
		public LandpContext landp() {
			return getRuleContext(LandpContext.class,0);
		}
		public LandpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_landp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterLandp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitLandp(this);
		}
	}

	public final LandpContext landp() throws RecognitionException {
		LandpContext _localctx = new LandpContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_landp);
		try {
			setState(193);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND:
				enterOuterAlt(_localctx, 1);
				{
				setState(188);
				match(AND);
				setState(189);
				comp();
				setState(190);
				landp();
				}
				break;
			case PA:
			case PC:
			case LLA:
			case LLC:
			case PYC:
			case COMA:
			case OR:
			case NUMERO:
			case INT:
			case DOUBLE:
			case CHAR:
			case WHILE:
			case FOR:
			case IF:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ComparadoresContext comparadores() {
			return getRuleContext(ComparadoresContext.class,0);
		}
		public CompContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterComp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitComp(this);
		}
	}

	public final CompContext comp() throws RecognitionException {
		CompContext _localctx = new CompContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_comp);
		try {
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(195);
				exp();
				setState(196);
				comparadores();
				setState(197);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(199);
				exp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			term();
			setState(203);
			e();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(compiladoresParser.SUMA, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public TerminalNode RESTA() { return getToken(compiladoresParser.RESTA, 0); }
		public EContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterE(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitE(this);
		}
	}

	public final EContext e() throws RecognitionException {
		EContext _localctx = new EContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_e);
		try {
			setState(214);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				match(SUMA);
				setState(206);
				term();
				setState(207);
				e();
				}
				break;
			case RESTA:
				enterOuterAlt(_localctx, 2);
				{
				setState(209);
				match(RESTA);
				setState(210);
				term();
				setState(211);
				e();
				}
				break;
			case PA:
			case PC:
			case LLA:
			case LLC:
			case PYC:
			case COMA:
			case AND:
			case OR:
			case MENOR:
			case MAYOR:
			case IGUAL:
			case MENORIG:
			case MAYORIG:
			case DIF:
			case NUMERO:
			case INT:
			case DOUBLE:
			case CHAR:
			case WHILE:
			case FOR:
			case IF:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_term);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			factor();
			setState(217);
			t();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TContext extends ParserRuleContext {
		public TerminalNode MULT() { return getToken(compiladoresParser.MULT, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public TContext t() {
			return getRuleContext(TContext.class,0);
		}
		public TerminalNode DIV() { return getToken(compiladoresParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(compiladoresParser.MOD, 0); }
		public TContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_t; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterT(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitT(this);
		}
	}

	public final TContext t() throws RecognitionException {
		TContext _localctx = new TContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_t);
		try {
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULT:
				enterOuterAlt(_localctx, 1);
				{
				setState(219);
				match(MULT);
				setState(220);
				factor();
				setState(221);
				t();
				}
				break;
			case DIV:
				enterOuterAlt(_localctx, 2);
				{
				setState(223);
				match(DIV);
				setState(224);
				factor();
				setState(225);
				t();
				}
				break;
			case MOD:
				enterOuterAlt(_localctx, 3);
				{
				setState(227);
				match(MOD);
				setState(228);
				factor();
				setState(229);
				t();
				}
				break;
			case PA:
			case PC:
			case LLA:
			case LLC:
			case PYC:
			case COMA:
			case SUMA:
			case RESTA:
			case AND:
			case OR:
			case MENOR:
			case MAYOR:
			case IGUAL:
			case MENORIG:
			case MAYORIG:
			case DIF:
			case NUMERO:
			case INT:
			case DOUBLE:
			case CHAR:
			case WHILE:
			case FOR:
			case IF:
			case RETURN:
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode NUMERO() { return getToken(compiladoresParser.NUMERO, 0); }
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public UsofuncionContext usofuncion() {
			return getRuleContext(UsofuncionContext.class,0);
		}
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterFactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitFactor(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_factor);
		try {
			setState(241);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				match(NUMERO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(235);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(236);
				usofuncion();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(237);
				match(PA);
				setState(238);
				exp();
				setState(239);
				match(PC);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IwhileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(compiladoresParser.WHILE, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public TerminalNode LLA() { return getToken(compiladoresParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladoresParser.LLC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IwhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iwhile; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIwhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIwhile(this);
		}
	}

	public final IwhileContext iwhile() throws RecognitionException {
		IwhileContext _localctx = new IwhileContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_iwhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(WHILE);
			setState(244);
			match(PA);
			setState(245);
			cond();
			setState(246);
			match(PC);
			setState(252);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(247);
				match(LLA);
				setState(248);
				instrucciones();
				setState(249);
				match(LLC);
				}
				break;
			case 2:
				{
				setState(251);
				instruccion();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IifContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(compiladoresParser.IF, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public TerminalNode LLA() { return getToken(compiladoresParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladoresParser.LLC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iif; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIif(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIif(this);
		}
	}

	public final IifContext iif() throws RecognitionException {
		IifContext _localctx = new IifContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_iif);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(IF);
			setState(255);
			match(PA);
			setState(256);
			cond();
			setState(257);
			match(PC);
			setState(263);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(258);
				match(LLA);
				setState(259);
				instrucciones();
				setState(260);
				match(LLC);
				}
				break;
			case 2:
				{
				setState(262);
				instruccion();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IforContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(compiladoresParser.FOR, 0); }
		public TerminalNode PA() { return getToken(compiladoresParser.PA, 0); }
		public InitContext init() {
			return getRuleContext(InitContext.class,0);
		}
		public List<TerminalNode> PYC() { return getTokens(compiladoresParser.PYC); }
		public TerminalNode PYC(int i) {
			return getToken(compiladoresParser.PYC, i);
		}
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public IterContext iter() {
			return getRuleContext(IterContext.class,0);
		}
		public TerminalNode PC() { return getToken(compiladoresParser.PC, 0); }
		public TerminalNode LLA() { return getToken(compiladoresParser.LLA, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLC() { return getToken(compiladoresParser.LLC, 0); }
		public InstruccionContext instruccion() {
			return getRuleContext(InstruccionContext.class,0);
		}
		public IforContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIfor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIfor(this);
		}
	}

	public final IforContext ifor() throws RecognitionException {
		IforContext _localctx = new IforContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_ifor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			match(FOR);
			setState(266);
			match(PA);
			setState(267);
			init();
			setState(268);
			match(PYC);
			setState(269);
			cond();
			setState(270);
			match(PYC);
			setState(271);
			iter();
			setState(272);
			match(PC);
			setState(278);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(273);
				match(LLA);
				setState(274);
				instrucciones();
				setState(275);
				match(LLC);
				}
				break;
			case 2:
				{
				setState(277);
				instruccion();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public TdatoContext tdato() {
			return getRuleContext(TdatoContext.class,0);
		}
		public InitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitInit(this);
		}
	}

	public final InitContext init() throws RecognitionException {
		InitContext _localctx = new InitContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_init);
		try {
			setState(293);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(280);
				match(ID);
				setState(281);
				match(ASIG);
				setState(282);
				opal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(283);
				tdato();
				setState(284);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(286);
				tdato();
				setState(287);
				match(ID);
				setState(288);
				match(ASIG);
				setState(289);
				opal();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(291);
				opal();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondContext extends ParserRuleContext {
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterCond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitCond(this);
		}
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			opal();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IterContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(compiladoresParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(compiladoresParser.ASIG, 0); }
		public OpalContext opal() {
			return getRuleContext(OpalContext.class,0);
		}
		public IterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).enterIter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof compiladoresListener ) ((compiladoresListener)listener).exitIter(this);
		}
	}

	public final IterContext iter() throws RecognitionException {
		IterContext _localctx = new IterContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_iter);
		try {
			setState(302);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(297);
				match(ID);
				setState(298);
				match(ASIG);
				setState(299);
				opal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(300);
				opal();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u0131\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0005"+
		"\u0003L\b\u0003\n\u0003\f\u0003O\t\u0003\u0001\u0003\u0005\u0003R\b\u0003"+
		"\n\u0003\f\u0003U\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005e\b\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"l\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bw\b\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0003\t~\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n"+
		"\u0084\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u008e\b\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0003\r\u0097\b\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00a3\b\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0003\u0013\u00b8\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00c2"+
		"\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003"+
		"\u0016\u00c9\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0003\u0018\u00d7\b\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0003\u001a\u00e9\b\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u00f2"+
		"\b\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u00fd\b\u001c\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0108\b\u001d\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003"+
		"\u001e\u0117\b\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0126\b\u001f\u0001 \u0001"+
		" \u0001!\u0001!\u0001!\u0001!\u0001!\u0003!\u012f\b!\u0001!\u0000\u0000"+
		"\"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,.02468:<>@B\u0000\u0003\u0001\u0000\u0010\u0015\u0002"+
		"\u0000\u0017\u0018\u001a\u001a\u0003\u0000\u0017\u0018\u001a\u001a\u001c"+
		"\u001c\u0133\u0000D\u0001\u0000\u0000\u0000\u0002F\u0001\u0000\u0000\u0000"+
		"\u0004H\u0001\u0000\u0000\u0000\u0006M\u0001\u0000\u0000\u0000\bX\u0001"+
		"\u0000\u0000\u0000\nd\u0001\u0000\u0000\u0000\fk\u0001\u0000\u0000\u0000"+
		"\u000em\u0001\u0000\u0000\u0000\u0010v\u0001\u0000\u0000\u0000\u0012}"+
		"\u0001\u0000\u0000\u0000\u0014\u0083\u0001\u0000\u0000\u0000\u0016\u008d"+
		"\u0001\u0000\u0000\u0000\u0018\u008f\u0001\u0000\u0000\u0000\u001a\u0096"+
		"\u0001\u0000\u0000\u0000\u001c\u00a2\u0001\u0000\u0000\u0000\u001e\u00a4"+
		"\u0001\u0000\u0000\u0000 \u00a9\u0001\u0000\u0000\u0000\"\u00ad\u0001"+
		"\u0000\u0000\u0000$\u00af\u0001\u0000\u0000\u0000&\u00b7\u0001\u0000\u0000"+
		"\u0000(\u00b9\u0001\u0000\u0000\u0000*\u00c1\u0001\u0000\u0000\u0000,"+
		"\u00c8\u0001\u0000\u0000\u0000.\u00ca\u0001\u0000\u0000\u00000\u00d6\u0001"+
		"\u0000\u0000\u00002\u00d8\u0001\u0000\u0000\u00004\u00e8\u0001\u0000\u0000"+
		"\u00006\u00f1\u0001\u0000\u0000\u00008\u00f3\u0001\u0000\u0000\u0000:"+
		"\u00fe\u0001\u0000\u0000\u0000<\u0109\u0001\u0000\u0000\u0000>\u0125\u0001"+
		"\u0000\u0000\u0000@\u0127\u0001\u0000\u0000\u0000B\u012e\u0001\u0000\u0000"+
		"\u0000DE\u0007\u0000\u0000\u0000E\u0001\u0001\u0000\u0000\u0000FG\u0007"+
		"\u0001\u0000\u0000G\u0003\u0001\u0000\u0000\u0000HI\u0007\u0002\u0000"+
		"\u0000I\u0005\u0001\u0000\u0000\u0000JL\u0003\u001c\u000e\u0000KJ\u0001"+
		"\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000"+
		"MN\u0001\u0000\u0000\u0000NS\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000"+
		"\u0000PR\u0003\b\u0004\u0000QP\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000"+
		"\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TV\u0001\u0000"+
		"\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0005\u0000\u0000\u0001W\u0007"+
		"\u0001\u0000\u0000\u0000XY\u0003\u0004\u0002\u0000YZ\u0005#\u0000\u0000"+
		"Z[\u0005\u0001\u0000\u0000[\\\u0003\n\u0005\u0000\\]\u0005\u0002\u0000"+
		"\u0000]^\u0003\u0018\f\u0000^\t\u0001\u0000\u0000\u0000_`\u0003\u0002"+
		"\u0001\u0000`a\u0005#\u0000\u0000ab\u0003\f\u0006\u0000be\u0001\u0000"+
		"\u0000\u0000ce\u0001\u0000\u0000\u0000d_\u0001\u0000\u0000\u0000dc\u0001"+
		"\u0000\u0000\u0000e\u000b\u0001\u0000\u0000\u0000fg\u0005\u0007\u0000"+
		"\u0000gh\u0003\n\u0005\u0000hi\u0003\f\u0006\u0000il\u0001\u0000\u0000"+
		"\u0000jl\u0001\u0000\u0000\u0000kf\u0001\u0000\u0000\u0000kj\u0001\u0000"+
		"\u0000\u0000l\r\u0001\u0000\u0000\u0000mn\u0005#\u0000\u0000no\u0005\u0001"+
		"\u0000\u0000op\u0003\u0010\b\u0000pq\u0005\u0002\u0000\u0000q\u000f\u0001"+
		"\u0000\u0000\u0000rs\u0003\"\u0011\u0000st\u0003\u0012\t\u0000tw\u0001"+
		"\u0000\u0000\u0000uw\u0001\u0000\u0000\u0000vr\u0001\u0000\u0000\u0000"+
		"vu\u0001\u0000\u0000\u0000w\u0011\u0001\u0000\u0000\u0000xy\u0005\u0007"+
		"\u0000\u0000yz\u0003\u0010\b\u0000z{\u0003\u0012\t\u0000{~\u0001\u0000"+
		"\u0000\u0000|~\u0001\u0000\u0000\u0000}x\u0001\u0000\u0000\u0000}|\u0001"+
		"\u0000\u0000\u0000~\u0013\u0001\u0000\u0000\u0000\u007f\u0080\u0003\u0016"+
		"\u000b\u0000\u0080\u0081\u0003\u0014\n\u0000\u0081\u0084\u0001\u0000\u0000"+
		"\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083\u007f\u0001\u0000\u0000"+
		"\u0000\u0083\u0082\u0001\u0000\u0000\u0000\u0084\u0015\u0001\u0000\u0000"+
		"\u0000\u0085\u008e\u0003\u001c\u000e\u0000\u0086\u008e\u0003\u001a\r\u0000"+
		"\u0087\u008e\u0003\u0018\f\u0000\u0088\u008e\u0003\u001e\u000f\u0000\u0089"+
		"\u008e\u0003\u000e\u0007\u0000\u008a\u008e\u0003\"\u0011\u0000\u008b\u008e"+
		"\u0003 \u0010\u0000\u008c\u008e\u0005\u0005\u0000\u0000\u008d\u0085\u0001"+
		"\u0000\u0000\u0000\u008d\u0086\u0001\u0000\u0000\u0000\u008d\u0087\u0001"+
		"\u0000\u0000\u0000\u008d\u0088\u0001\u0000\u0000\u0000\u008d\u0089\u0001"+
		"\u0000\u0000\u0000\u008d\u008a\u0001\u0000\u0000\u0000\u008d\u008b\u0001"+
		"\u0000\u0000\u0000\u008d\u008c\u0001\u0000\u0000\u0000\u008e\u0017\u0001"+
		"\u0000\u0000\u0000\u008f\u0090\u0005\u0003\u0000\u0000\u0090\u0091\u0003"+
		"\u0014\n\u0000\u0091\u0092\u0005\u0004\u0000\u0000\u0092\u0019\u0001\u0000"+
		"\u0000\u0000\u0093\u0097\u00038\u001c\u0000\u0094\u0097\u0003<\u001e\u0000"+
		"\u0095\u0097\u0003:\u001d\u0000\u0096\u0093\u0001\u0000\u0000\u0000\u0096"+
		"\u0094\u0001\u0000\u0000\u0000\u0096\u0095\u0001\u0000\u0000\u0000\u0097"+
		"\u001b\u0001\u0000\u0000\u0000\u0098\u0099\u0003\u0002\u0001\u0000\u0099"+
		"\u009a\u0005#\u0000\u0000\u009a\u009b\u0005\u0005\u0000\u0000\u009b\u00a3"+
		"\u0001\u0000\u0000\u0000\u009c\u009d\u0003\u0002\u0001\u0000\u009d\u009e"+
		"\u0005#\u0000\u0000\u009e\u009f\u0005\r\u0000\u0000\u009f\u00a0\u0003"+
		"\"\u0011\u0000\u00a0\u00a1\u0005\u0005\u0000\u0000\u00a1\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a2\u0098\u0001\u0000\u0000\u0000\u00a2\u009c\u0001\u0000"+
		"\u0000\u0000\u00a3\u001d\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005#\u0000"+
		"\u0000\u00a5\u00a6\u0005\r\u0000\u0000\u00a6\u00a7\u0003\"\u0011\u0000"+
		"\u00a7\u00a8\u0005\u0005\u0000\u0000\u00a8\u001f\u0001\u0000\u0000\u0000"+
		"\u00a9\u00aa\u0005!\u0000\u0000\u00aa\u00ab\u0003\"\u0011\u0000\u00ab"+
		"\u00ac\u0005\u0005\u0000\u0000\u00ac!\u0001\u0000\u0000\u0000\u00ad\u00ae"+
		"\u0003$\u0012\u0000\u00ae#\u0001\u0000\u0000\u0000\u00af\u00b0\u0003("+
		"\u0014\u0000\u00b0\u00b1\u0003&\u0013\u0000\u00b1%\u0001\u0000\u0000\u0000"+
		"\u00b2\u00b3\u0005\u000f\u0000\u0000\u00b3\u00b4\u0003(\u0014\u0000\u00b4"+
		"\u00b5\u0003&\u0013\u0000\u00b5\u00b8\u0001\u0000\u0000\u0000\u00b6\u00b8"+
		"\u0001\u0000\u0000\u0000\u00b7\u00b2\u0001\u0000\u0000\u0000\u00b7\u00b6"+
		"\u0001\u0000\u0000\u0000\u00b8\'\u0001\u0000\u0000\u0000\u00b9\u00ba\u0003"+
		",\u0016\u0000\u00ba\u00bb\u0003*\u0015\u0000\u00bb)\u0001\u0000\u0000"+
		"\u0000\u00bc\u00bd\u0005\u000e\u0000\u0000\u00bd\u00be\u0003,\u0016\u0000"+
		"\u00be\u00bf\u0003*\u0015\u0000\u00bf\u00c2\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c2\u0001\u0000\u0000\u0000\u00c1\u00bc\u0001\u0000\u0000\u0000\u00c1"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c2+\u0001\u0000\u0000\u0000\u00c3\u00c4"+
		"\u0003.\u0017\u0000\u00c4\u00c5\u0003\u0000\u0000\u0000\u00c5\u00c6\u0003"+
		".\u0017\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c9\u0003.\u0017"+
		"\u0000\u00c8\u00c3\u0001\u0000\u0000\u0000\u00c8\u00c7\u0001\u0000\u0000"+
		"\u0000\u00c9-\u0001\u0000\u0000\u0000\u00ca\u00cb\u00032\u0019\u0000\u00cb"+
		"\u00cc\u00030\u0018\u0000\u00cc/\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005"+
		"\b\u0000\u0000\u00ce\u00cf\u00032\u0019\u0000\u00cf\u00d0\u00030\u0018"+
		"\u0000\u00d0\u00d7\u0001\u0000\u0000\u0000\u00d1\u00d2\u0005\t\u0000\u0000"+
		"\u00d2\u00d3\u00032\u0019\u0000\u00d3\u00d4\u00030\u0018\u0000\u00d4\u00d7"+
		"\u0001\u0000\u0000\u0000\u00d5\u00d7\u0001\u0000\u0000\u0000\u00d6\u00cd"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d1\u0001\u0000\u0000\u0000\u00d6\u00d5"+
		"\u0001\u0000\u0000\u0000\u00d71\u0001\u0000\u0000\u0000\u00d8\u00d9\u0003"+
		"6\u001b\u0000\u00d9\u00da\u00034\u001a\u0000\u00da3\u0001\u0000\u0000"+
		"\u0000\u00db\u00dc\u0005\n\u0000\u0000\u00dc\u00dd\u00036\u001b\u0000"+
		"\u00dd\u00de\u00034\u001a\u0000\u00de\u00e9\u0001\u0000\u0000\u0000\u00df"+
		"\u00e0\u0005\u000b\u0000\u0000\u00e0\u00e1\u00036\u001b\u0000\u00e1\u00e2"+
		"\u00034\u001a\u0000\u00e2\u00e9\u0001\u0000\u0000\u0000\u00e3\u00e4\u0005"+
		"\f\u0000\u0000\u00e4\u00e5\u00036\u001b\u0000\u00e5\u00e6\u00034\u001a"+
		"\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e9\u0001\u0000\u0000"+
		"\u0000\u00e8\u00db\u0001\u0000\u0000\u0000\u00e8\u00df\u0001\u0000\u0000"+
		"\u0000\u00e8\u00e3\u0001\u0000\u0000\u0000\u00e8\u00e7\u0001\u0000\u0000"+
		"\u0000\u00e95\u0001\u0000\u0000\u0000\u00ea\u00f2\u0005\u0016\u0000\u0000"+
		"\u00eb\u00f2\u0005#\u0000\u0000\u00ec\u00f2\u0003\u000e\u0007\u0000\u00ed"+
		"\u00ee\u0005\u0001\u0000\u0000\u00ee\u00ef\u0003.\u0017\u0000\u00ef\u00f0"+
		"\u0005\u0002\u0000\u0000\u00f0\u00f2\u0001\u0000\u0000\u0000\u00f1\u00ea"+
		"\u0001\u0000\u0000\u0000\u00f1\u00eb\u0001\u0000\u0000\u0000\u00f1\u00ec"+
		"\u0001\u0000\u0000\u0000\u00f1\u00ed\u0001\u0000\u0000\u0000\u00f27\u0001"+
		"\u0000\u0000\u0000\u00f3\u00f4\u0005\u001d\u0000\u0000\u00f4\u00f5\u0005"+
		"\u0001\u0000\u0000\u00f5\u00f6\u0003@ \u0000\u00f6\u00fc\u0005\u0002\u0000"+
		"\u0000\u00f7\u00f8\u0005\u0003\u0000\u0000\u00f8\u00f9\u0003\u0014\n\u0000"+
		"\u00f9\u00fa\u0005\u0004\u0000\u0000\u00fa\u00fd\u0001\u0000\u0000\u0000"+
		"\u00fb\u00fd\u0003\u0016\u000b\u0000\u00fc\u00f7\u0001\u0000\u0000\u0000"+
		"\u00fc\u00fb\u0001\u0000\u0000\u0000\u00fd9\u0001\u0000\u0000\u0000\u00fe"+
		"\u00ff\u0005\u001f\u0000\u0000\u00ff\u0100\u0005\u0001\u0000\u0000\u0100"+
		"\u0101\u0003@ \u0000\u0101\u0107\u0005\u0002\u0000\u0000\u0102\u0103\u0005"+
		"\u0003\u0000\u0000\u0103\u0104\u0003\u0014\n\u0000\u0104\u0105\u0005\u0004"+
		"\u0000\u0000\u0105\u0108\u0001\u0000\u0000\u0000\u0106\u0108\u0003\u0016"+
		"\u000b\u0000\u0107\u0102\u0001\u0000\u0000\u0000\u0107\u0106\u0001\u0000"+
		"\u0000\u0000\u0108;\u0001\u0000\u0000\u0000\u0109\u010a\u0005\u001e\u0000"+
		"\u0000\u010a\u010b\u0005\u0001\u0000\u0000\u010b\u010c\u0003>\u001f\u0000"+
		"\u010c\u010d\u0005\u0005\u0000\u0000\u010d\u010e\u0003@ \u0000\u010e\u010f"+
		"\u0005\u0005\u0000\u0000\u010f\u0110\u0003B!\u0000\u0110\u0116\u0005\u0002"+
		"\u0000\u0000\u0111\u0112\u0005\u0003\u0000\u0000\u0112\u0113\u0003\u0014"+
		"\n\u0000\u0113\u0114\u0005\u0004\u0000\u0000\u0114\u0117\u0001\u0000\u0000"+
		"\u0000\u0115\u0117\u0003\u0016\u000b\u0000\u0116\u0111\u0001\u0000\u0000"+
		"\u0000\u0116\u0115\u0001\u0000\u0000\u0000\u0117=\u0001\u0000\u0000\u0000"+
		"\u0118\u0119\u0005#\u0000\u0000\u0119\u011a\u0005\r\u0000\u0000\u011a"+
		"\u0126\u0003\"\u0011\u0000\u011b\u011c\u0003\u0002\u0001\u0000\u011c\u011d"+
		"\u0005#\u0000\u0000\u011d\u0126\u0001\u0000\u0000\u0000\u011e\u011f\u0003"+
		"\u0002\u0001\u0000\u011f\u0120\u0005#\u0000\u0000\u0120\u0121\u0005\r"+
		"\u0000\u0000\u0121\u0122\u0003\"\u0011\u0000\u0122\u0126\u0001\u0000\u0000"+
		"\u0000\u0123\u0126\u0003\"\u0011\u0000\u0124\u0126\u0001\u0000\u0000\u0000"+
		"\u0125\u0118\u0001\u0000\u0000\u0000\u0125\u011b\u0001\u0000\u0000\u0000"+
		"\u0125\u011e\u0001\u0000\u0000\u0000\u0125\u0123\u0001\u0000\u0000\u0000"+
		"\u0125\u0124\u0001\u0000\u0000\u0000\u0126?\u0001\u0000\u0000\u0000\u0127"+
		"\u0128\u0003\"\u0011\u0000\u0128A\u0001\u0000\u0000\u0000\u0129\u012a"+
		"\u0005#\u0000\u0000\u012a\u012b\u0005\r\u0000\u0000\u012b\u012f\u0003"+
		"\"\u0011\u0000\u012c\u012f\u0003\"\u0011\u0000\u012d\u012f\u0001\u0000"+
		"\u0000\u0000\u012e\u0129\u0001\u0000\u0000\u0000\u012e\u012c\u0001\u0000"+
		"\u0000\u0000\u012e\u012d\u0001\u0000\u0000\u0000\u012fC\u0001\u0000\u0000"+
		"\u0000\u0015MSdkv}\u0083\u008d\u0096\u00a2\u00b7\u00c1\u00c8\u00d6\u00e8"+
		"\u00f1\u00fc\u0107\u0116\u0125\u012e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}