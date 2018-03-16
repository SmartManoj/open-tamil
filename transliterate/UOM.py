## -*- coding: utf-8 -*-
# (C) 2018 Muthiah Annamalai

# சென்னை பல்கலைக்கழக தமிழ் பேரகராதி
# University of Madras standard - Ref: http://dsal.uchicago.edu/dictionaries/tamil-lex/
# Twitter comment by Jean-Luc Chevilliard @JLC1956:
# 'There is no "umlaut" (umlaut would be ä, ü or ö, as in German). The #TranslitteratedTamil alphabet is: a ā i ī u ū e ē ai o ō au ḵ k ṅ c ñ ṭ ṇ t n p m y r l v ḻ ḷ ṟ ṉ.
# (#Cash might be debated ;-) and discussion won't fit in 280 characters :-)''
#
class ReverseTransliteration:
    table = {}
    table[u'அ'] = u'a'
    table[u'ஆ'] = u'ā'
    table[u'இ'] = u'i'
    table[u'ஈ'] = u'ī'
    table[u'உ'] = u'u'
    table[u'ஊ'] = u'ū'
    table[u'எ'] = u'e'
    table[u'ஏ'] = u'ē'
    table[u'ஐ'] = u'ai'
    table[u'ஒ'] = u'o'
    table[u'ஓ'] = u'ō'
    table[u'ஔ'] = u'au'
    table[u"ஃ"] = u'ak'

    table[u'க்'] = u'ik'
    table[u'ஞ்'] = u'iñ'
    table[u'ச்'] = u'ic'
    table[u'ங்'] = u'iṅ'
    table[u'த்'] = u'it'
    table[u'ன்'] = u'iṉ'
    table[u'ட்'] = u'it'
    table[u'ண்'] = u'iṇ'
    table[u'ப்'] = u'ip'
    table[u'ம்'] = u'im'
    table[u'ய்'] = u'iy'
    table[u'ர்'] = u'ir'
    table[u'ல்'] = u'il'
    table[u'வ்'] = u'iv'
    table[u'ள்'] = u'iḻ'
    table[u'ழ்'] = u'iḷ'
    table[u'ற்'] = u'iṟ'
    table[u'ந்'] = u'in'

    table[u'க'] = u'k'
    table[u'ஞ'] = u'ñ'
    table[u'ச'] = u'c'
    table[u'ங'] = u'ṅ'
    table[u'த'] = u't'
    table[u'ன'] = u'ṉ'
    table[u'ட'] = u'ṭ'
    table[u'ண'] = u'ṇ'
    table[u'ப'] = u'p'
    table[u'ம'] = u'm'
    table[u'ய'] = u'y'
    table[u'ர'] = u'r'
    table[u'ல'] = u'l'
    table[u'வ'] = u'v'
    table[u'ள'] = u'ḷ'
    table[u'ழ'] = u'ḻ'
    table[u'ற'] = u'ṟ'
    table[u'ந'] = u'n'
    table[u'கா']=u'kā'
    table[u'கி']=u'ki'
    table[u'கீ']=u'kī'
    table[u'கு']=u'ku'
    table[u'கூ']=u'kū'
    table[u'கெ']=u'ke'
    table[u'கே']=u'kē'
    table[u'கை']=u'kai'
    table[u'கொ']=u'ko'
    table[u'கோ']=u'kō'
    table[u'கௌ']=u'kau'
    table[u'சா']=u'cā'
    table[u'சி']=u'ci'
    table[u'சீ']=u'cī'
    table[u'சு']=u'cu'
    table[u'சூ']=u'cū'
    table[u'செ']=u'ce'
    table[u'சே']=u'cē'
    table[u'சை']=u'cai'
    table[u'சொ']=u'co'
    table[u'சோ']=u'cō'
    table[u'சௌ']=u'cau'
    table[u'டா']=u'tā'
    table[u'டி']=u'ti'
    table[u'டீ']=u'tī'
    table[u'டு']=u'tu'
    table[u'டூ']=u'tū'
    table[u'டெ']=u'te'
    table[u'டே']=u'tē'
    table[u'டை']=u'tai'
    table[u'டொ']=u'to'
    table[u'டோ']=u'tō'
    table[u'டௌ']=u'tau'
    table[u'தா']=u'tā'
    table[u'தி']=u'ti'
    table[u'தீ']=u'tī'
    table[u'து']=u'tu'
    table[u'தூ']=u'tū'
    table[u'தெ']=u'te'
    table[u'தே']=u'tē'
    table[u'தை']=u'tai'
    table[u'தொ']=u'to'
    table[u'தோ']=u'tō'
    table[u'தௌ']=u'tau'
    table[u'பா']=u'pā'
    table[u'பி']=u'pi'
    table[u'பீ']=u'pī'
    table[u'பு']=u'pu'
    table[u'பூ']=u'pū'
    table[u'பெ']=u'pe'
    table[u'பே']=u'pē'
    table[u'பை']=u'pai'
    table[u'பொ']=u'po'
    table[u'போ']=u'pō'
    table[u'பௌ']=u'pau'
    table[u'றா']=u'ṟā'
    table[u'றி']=u'ṟi'
    table[u'றீ']=u'ṟī'
    table[u'று']=u'ṟu'
    table[u'றூ']=u'ṟū'
    table[u'றெ']=u'ṟe'
    table[u'றே']=u'ṟē'
    table[u'றை']=u'ṟai'
    table[u'றொ']=u'ṟo'
    table[u'றோ']=u'ṟō'
    table[u'றௌ']=u'ṟau'
    table[u'ஞா']=u'ñā'
    table[u'ஞி']=u'ñi'
    table[u'ஞீ']=u'ñī'
    table[u'ஞு']=u'ñu'
    table[u'ஞூ']=u'ñū'
    table[u'ஞெ']=u'ñe'
    table[u'ஞே']=u'ñē'
    table[u'ஞை']=u'ñai'
    table[u'ஞொ']=u'ño'
    table[u'ஞோ']=u'ñō'
    table[u'ஞௌ']=u'ñau'
    table[u'ஙா']=u'ṅā'
    table[u'ஙி']=u'ṅi'
    table[u'ஙீ']=u'ṅī'
    table[u'ஙு']=u'ṅu'
    table[u'ஙூ']=u'ṅū'
    table[u'ஙெ']=u'ṅe'
    table[u'ஙே']=u'ṅē'
    table[u'ஙை']=u'ṅai'
    table[u'ஙொ']=u'ṅo'
    table[u'ஙோ']=u'ṅō'
    table[u'ஙௌ']=u'ṅau'
    table[u'ணா']=u'ṇā'
    table[u'ணி']=u'ṇi'
    table[u'ணீ']=u'ṇī'
    table[u'ணு']=u'ṇu'
    table[u'ணூ']=u'ṇū'
    table[u'ணெ']=u'ṇe'
    table[u'ணே']=u'ṇē'
    table[u'ணை']=u'ṇai'
    table[u'ணொ']=u'ṇo'
    table[u'ணோ']=u'ṇō'
    table[u'ணௌ']=u'ṇau'
    table[u'நா']=u'nā'
    table[u'நி']=u'ni'
    table[u'நீ']=u'nī'
    table[u'நு']=u'nu'
    table[u'நூ']=u'nū'
    table[u'நெ']=u'ne'
    table[u'நே']=u'nē'
    table[u'நை']=u'nai'
    table[u'நொ']=u'no'
    table[u'நோ']=u'nō'
    table[u'நௌ']=u'nau'
    table[u'மா']=u'mā'
    table[u'மி']=u'mi'
    table[u'மீ']=u'mī'
    table[u'மு']=u'mu'
    table[u'மூ']=u'mū'
    table[u'மெ']=u'me'
    table[u'மே']=u'mē'
    table[u'மை']=u'mai'
    table[u'மொ']=u'mo'
    table[u'மோ']=u'mō'
    table[u'மௌ']=u'mau'
    table[u'னா']=u'ṉā'
    table[u'னி']=u'ṉi'
    table[u'னீ']=u'ṉī'
    table[u'னு']=u'ṉu'
    table[u'னூ']=u'ṉū'
    table[u'னெ']=u'ṉe'
    table[u'னே']=u'ṉē'
    table[u'னை']=u'ṉai'
    table[u'னொ']=u'ṉo'
    table[u'னோ']=u'ṉō'
    table[u'னௌ']=u'ṉau'
    table[u'யா']=u'yā'
    table[u'யி']=u'yi'
    table[u'யீ']=u'yī'
    table[u'யு']=u'yu'
    table[u'யூ']=u'yū'
    table[u'யெ']=u'ye'
    table[u'யே']=u'yē'
    table[u'யை']=u'yai'
    table[u'யொ']=u'yo'
    table[u'யோ']=u'yō'
    table[u'யௌ']=u'yau'
    table[u'ரா']=u'rā'
    table[u'ரி']=u'ri'
    table[u'ரீ']=u'rī'
    table[u'ரு']=u'ru'
    table[u'ரூ']=u'rū'
    table[u'ரெ']=u're'
    table[u'ரே']=u'rē'
    table[u'ரை']=u'rai'
    table[u'ரொ']=u'ro'
    table[u'ரோ']=u'rō'
    table[u'ரௌ']=u'rau'
    table[u'லா']=u'lā'
    table[u'லி']=u'li'
    table[u'லீ']=u'lī'
    table[u'லு']=u'lu'
    table[u'லூ']=u'lū'
    table[u'லெ']=u'le'
    table[u'லே']=u'lē'
    table[u'லை']=u'lai'
    table[u'லொ']=u'lo'
    table[u'லோ']=u'lō'
    table[u'லௌ']=u'lau'
    table[u'வா']=u'vā'
    table[u'வி']=u'vi'
    table[u'வீ']=u'vī'
    table[u'வு']=u'vu'
    table[u'வூ']=u'vū'
    table[u'வெ']=u've'
    table[u'வே']=u'vē'
    table[u'வை']=u'vai'
    table[u'வொ']=u'vo'
    table[u'வோ']=u'vō'
    table[u'வௌ']=u'vau'
    table[u'ழா']=u'ḷā'
    table[u'ழி']=u'ḷi'
    table[u'ழீ']=u'ḷī'
    table[u'ழு']=u'ḷu'
    table[u'ழூ']=u'ḷū'
    table[u'ழெ']=u'ḷe'
    table[u'ழே']=u'ḷē'
    table[u'ழை']=u'ḷai'
    table[u'ழொ']=u'ḷo'
    table[u'ழோ']=u'ḷō'
    table[u'ழௌ']=u'ḷau'
    table[u'ளா']=u'ḻā'
    table[u'ளி']=u'ḻi'
    table[u'ளீ']=u'ḻī'
    table[u'ளு']=u'ḻu'
    table[u'ளூ']=u'ḻū'
    table[u'ளெ']=u'ḻe'
    table[u'ளே']=u'ḻē'
    table[u'ளை']=u'ḻai'
    table[u'ளொ']=u'ḻo'
    table[u'ளோ']=u'ḻō'
    table[u'ளௌ']=u'ḻau'


#if __name__ == u"__main__":
#    from tamil.utf8 import agaram_letters,uyirmei_letters, splitMeiUyir,compare_words_lexicographic
#    for um in sorted(list(set(uyirmei_letters)-set(agaram_letters)),compare_words_lexicographic):
#        u,m=splitMeiUyir(um)
#        tl = ReverseTransliteration.table[u][1:]+ReverseTransliteration.table[m]
#        print(u"table[u'%s']=u'%s'"%(um,tl))

#meta-..
#if __name__ == u"__main__":
#    from tamil import utf8
#    for l in utf8.uyirmei_letters:
#        mei,uyir = utf8.splitMeiUyir(l)
#        agaram = utf8.mei_to_agaram(mei)
#        print(u"    table[u'%s'] = u'%s'"%(l,ReverseTransliteration.table[agaram]+ReverseTransliteration.table[uyir]))
#    keys = ReverseTransliteration.table.keys()
#    for k in sorted(keys,utf8.compare_words_lexicographic):
#        v = ReverseTransliteration.table[k]
#        print(u"    table[u'%s'] = u'%s'"%(v,k))

class Transliteration:
    table = {}
    table[u'a'] = u'அ'
    table[u'ā'] = u'ஆ'
    table[u'i'] = u'இ'
    table[u'ī'] = u'ஈ'
    table[u'u'] = u'உ'
    table[u'ū'] = u'ஊ'
    table[u'e'] = u'எ'
    table[u'ē'] = u'ஏ'
    table[u'ai'] = u'ஐ'
    table[u'o'] = u'ஒ'
    table[u'ō'] = u'ஓ'
    table[u'au'] = u'ஔ'
    table[u'ak'] = u'ஃ'
    table[u'k'] = u'க'
    table[u'ik'] = u'க்'
    table[u'kā'] = u'கா'
    table[u'ki'] = u'கி'
    table[u'kī'] = u'கீ'
    table[u'ku'] = u'கு'
    table[u'kū'] = u'கூ'
    table[u'ke'] = u'கெ'
    table[u'kē'] = u'கே'
    table[u'kai'] = u'கை'
    table[u'ko'] = u'கொ'
    table[u'kō'] = u'கோ'
    table[u'kau'] = u'கௌ'
    table[u'c'] = u'ச'
    table[u'ic'] = u'ச்'
    table[u'cā'] = u'சா'
    table[u'ci'] = u'சி'
    table[u'cī'] = u'சீ'
    table[u'cu'] = u'சு'
    table[u'cū'] = u'சூ'
    table[u'ce'] = u'செ'
    table[u'cē'] = u'சே'
    table[u'cai'] = u'சை'
    table[u'co'] = u'சொ'
    table[u'cō'] = u'சோ'
    table[u'cau'] = u'சௌ'
    table[u'ṭ'] = u'ட'
    table[u'it'] = u'ட்'
    table[u'tā'] = u'டா'
    table[u'ti'] = u'டி'
    table[u'tī'] = u'டீ'
    table[u'tu'] = u'டு'
    table[u'tū'] = u'டூ'
    table[u'te'] = u'டெ'
    table[u'tē'] = u'டே'
    table[u'tai'] = u'டை'
    table[u'to'] = u'டொ'
    table[u'tō'] = u'டோ'
    table[u'tau'] = u'டௌ'
    table[u't'] = u'த'
    table[u'it'] = u'த்'
    table[u'tā'] = u'தா'
    table[u'ti'] = u'தி'
    table[u'tī'] = u'தீ'
    table[u'tu'] = u'து'
    table[u'tū'] = u'தூ'
    table[u'te'] = u'தெ'
    table[u'tē'] = u'தே'
    table[u'tai'] = u'தை'
    table[u'to'] = u'தொ'
    table[u'tō'] = u'தோ'
    table[u'tau'] = u'தௌ'
    table[u'p'] = u'ப'
    table[u'ip'] = u'ப்'
    table[u'pā'] = u'பா'
    table[u'pi'] = u'பி'
    table[u'pī'] = u'பீ'
    table[u'pu'] = u'பு'
    table[u'pū'] = u'பூ'
    table[u'pe'] = u'பெ'
    table[u'pē'] = u'பே'
    table[u'pai'] = u'பை'
    table[u'po'] = u'பொ'
    table[u'pō'] = u'போ'
    table[u'pau'] = u'பௌ'
    table[u'ṟ'] = u'ற'
    table[u'iṟ'] = u'ற்'
    table[u'ṟā'] = u'றா'
    table[u'ṟi'] = u'றி'
    table[u'ṟī'] = u'றீ'
    table[u'ṟu'] = u'று'
    table[u'ṟū'] = u'றூ'
    table[u'ṟe'] = u'றெ'
    table[u'ṟē'] = u'றே'
    table[u'ṟai'] = u'றை'
    table[u'ṟo'] = u'றொ'
    table[u'ṟō'] = u'றோ'
    table[u'ṟau'] = u'றௌ'
    table[u'ñ'] = u'ஞ'
    table[u'iñ'] = u'ஞ்'
    table[u'ñā'] = u'ஞா'
    table[u'ñi'] = u'ஞி'
    table[u'ñī'] = u'ஞீ'
    table[u'ñu'] = u'ஞு'
    table[u'ñū'] = u'ஞூ'
    table[u'ñe'] = u'ஞெ'
    table[u'ñē'] = u'ஞே'
    table[u'ñai'] = u'ஞை'
    table[u'ño'] = u'ஞொ'
    table[u'ñō'] = u'ஞோ'
    table[u'ñau'] = u'ஞௌ'
    table[u'ṅ'] = u'ங'
    table[u'iṅ'] = u'ங்'
    table[u'ṅā'] = u'ஙா'
    table[u'ṅi'] = u'ஙி'
    table[u'ṅī'] = u'ஙீ'
    table[u'ṅu'] = u'ஙு'
    table[u'ṅū'] = u'ஙூ'
    table[u'ṅe'] = u'ஙெ'
    table[u'ṅē'] = u'ஙே'
    table[u'ṅai'] = u'ஙை'
    table[u'ṅo'] = u'ஙொ'
    table[u'ṅō'] = u'ஙோ'
    table[u'ṅau'] = u'ஙௌ'
    table[u'ṇ'] = u'ண'
    table[u'iṇ'] = u'ண்'
    table[u'ṇā'] = u'ணா'
    table[u'ṇi'] = u'ணி'
    table[u'ṇī'] = u'ணீ'
    table[u'ṇu'] = u'ணு'
    table[u'ṇū'] = u'ணூ'
    table[u'ṇe'] = u'ணெ'
    table[u'ṇē'] = u'ணே'
    table[u'ṇai'] = u'ணை'
    table[u'ṇo'] = u'ணொ'
    table[u'ṇō'] = u'ணோ'
    table[u'ṇau'] = u'ணௌ'
    table[u'n'] = u'ந'
    table[u'in'] = u'ந்'
    table[u'nā'] = u'நா'
    table[u'ni'] = u'நி'
    table[u'nī'] = u'நீ'
    table[u'nu'] = u'நு'
    table[u'nū'] = u'நூ'
    table[u'ne'] = u'நெ'
    table[u'nē'] = u'நே'
    table[u'nai'] = u'நை'
    table[u'no'] = u'நொ'
    table[u'nō'] = u'நோ'
    table[u'nau'] = u'நௌ'
    table[u'm'] = u'ம'
    table[u'im'] = u'ம்'
    table[u'mā'] = u'மா'
    table[u'mi'] = u'மி'
    table[u'mī'] = u'மீ'
    table[u'mu'] = u'மு'
    table[u'mū'] = u'மூ'
    table[u'me'] = u'மெ'
    table[u'mē'] = u'மே'
    table[u'mai'] = u'மை'
    table[u'mo'] = u'மொ'
    table[u'mō'] = u'மோ'
    table[u'mau'] = u'மௌ'
    table[u'ṉ'] = u'ன'
    table[u'iṉ'] = u'ன்'
    table[u'ṉā'] = u'னா'
    table[u'ṉi'] = u'னி'
    table[u'ṉī'] = u'னீ'
    table[u'ṉu'] = u'னு'
    table[u'ṉū'] = u'னூ'
    table[u'ṉe'] = u'னெ'
    table[u'ṉē'] = u'னே'
    table[u'ṉai'] = u'னை'
    table[u'ṉo'] = u'னொ'
    table[u'ṉō'] = u'னோ'
    table[u'ṉau'] = u'னௌ'
    table[u'y'] = u'ய'
    table[u'iy'] = u'ய்'
    table[u'yā'] = u'யா'
    table[u'yi'] = u'யி'
    table[u'yī'] = u'யீ'
    table[u'yu'] = u'யு'
    table[u'yū'] = u'யூ'
    table[u'ye'] = u'யெ'
    table[u'yē'] = u'யே'
    table[u'yai'] = u'யை'
    table[u'yo'] = u'யொ'
    table[u'yō'] = u'யோ'
    table[u'yau'] = u'யௌ'
    table[u'r'] = u'ர'
    table[u'ir'] = u'ர்'
    table[u'rā'] = u'ரா'
    table[u'ri'] = u'ரி'
    table[u'rī'] = u'ரீ'
    table[u'ru'] = u'ரு'
    table[u'rū'] = u'ரூ'
    table[u're'] = u'ரெ'
    table[u'rē'] = u'ரே'
    table[u'rai'] = u'ரை'
    table[u'ro'] = u'ரொ'
    table[u'rō'] = u'ரோ'
    table[u'rau'] = u'ரௌ'
    table[u'l'] = u'ல'
    table[u'il'] = u'ல்'
    table[u'lā'] = u'லா'
    table[u'li'] = u'லி'
    table[u'lī'] = u'லீ'
    table[u'lu'] = u'லு'
    table[u'lū'] = u'லூ'
    table[u'le'] = u'லெ'
    table[u'lē'] = u'லே'
    table[u'lai'] = u'லை'
    table[u'lo'] = u'லொ'
    table[u'lō'] = u'லோ'
    table[u'lau'] = u'லௌ'
    table[u'v'] = u'வ'
    table[u'iv'] = u'வ்'
    table[u'vā'] = u'வா'
    table[u'vi'] = u'வி'
    table[u'vī'] = u'வீ'
    table[u'vu'] = u'வு'
    table[u'vū'] = u'வூ'
    table[u've'] = u'வெ'
    table[u'vē'] = u'வே'
    table[u'vai'] = u'வை'
    table[u'vo'] = u'வொ'
    table[u'vō'] = u'வோ'
    table[u'vau'] = u'வௌ'
    table[u'ḻ'] = u'ழ'
    table[u'iḷ'] = u'ழ்'
    table[u'ḷā'] = u'ழா'
    table[u'ḷi'] = u'ழி'
    table[u'ḷī'] = u'ழீ'
    table[u'ḷu'] = u'ழு'
    table[u'ḷū'] = u'ழூ'
    table[u'ḷe'] = u'ழெ'
    table[u'ḷē'] = u'ழே'
    table[u'ḷai'] = u'ழை'
    table[u'ḷo'] = u'ழொ'
    table[u'ḷō'] = u'ழோ'
    table[u'ḷau'] = u'ழௌ'
    table[u'ḷ'] = u'ள'
    table[u'iḻ'] = u'ள்'
    table[u'ḻā'] = u'ளா'
    table[u'ḻi'] = u'ளி'
    table[u'ḻī'] = u'ளீ'
    table[u'ḻu'] = u'ளு'
    table[u'ḻū'] = u'ளூ'
    table[u'ḻe'] = u'ளெ'
    table[u'ḻē'] = u'ளே'
    table[u'ḻai'] = u'ளை'
    table[u'ḻo'] = u'ளொ'
    table[u'ḻō'] = u'ளோ'
    table[u'ḻau'] = u'ளௌ'
    table[u'ku'] = u'கு'
    table[u'kū'] = u'கூ'
    table[u'ke'] = u'கெ'
    table[u'kē'] = u'கே'
    table[u'kai'] = u'கை'
    table[u'ko'] = u'கொ'
    table[u'kō'] = u'கோ'
    table[u'kau'] = u'கௌ'
    table[u'ca'] = u'ச'
    table[u'ic'] = u'ச்'
    table[u'cā'] = u'சா'
    table[u'ci'] = u'சி'
    table[u'cī'] = u'சீ'
    table[u'cu'] = u'சு'
    table[u'cū'] = u'சூ'
    table[u'ce'] = u'செ'
    table[u'cē'] = u'சே'
    table[u'cai'] = u'சை'
    table[u'co'] = u'சொ'
    table[u'cō'] = u'சோ'
    table[u'cau'] = u'சௌ'
    table[u'ta'] = u'ட'
    table[u'it'] = u'ட்'
    table[u'tā'] = u'டா'
    table[u'ti'] = u'டி'
    table[u'tī'] = u'டீ'
    table[u'tu'] = u'டு'
    table[u'tū'] = u'டூ'
    table[u'te'] = u'டெ'
    table[u'tē'] = u'டே'
    table[u'tai'] = u'டை'
    table[u'to'] = u'டொ'
    table[u'tō'] = u'டோ'
    table[u'tau'] = u'டௌ'
    table[u'ta'] = u'த'
    table[u'it'] = u'த்'
    table[u'tā'] = u'தா'
    table[u'ti'] = u'தி'
    table[u'tī'] = u'தீ'
    table[u'tu'] = u'து'
    table[u'tū'] = u'தூ'
    table[u'te'] = u'தெ'
    table[u'tē'] = u'தே'
    table[u'tai'] = u'தை'
    table[u'to'] = u'தொ'
    table[u'tō'] = u'தோ'
    table[u'tau'] = u'தௌ'
    table[u'pa'] = u'ப'
    table[u'ip'] = u'ப்'
    table[u'pā'] = u'பா'
    table[u'pi'] = u'பி'
    table[u'pī'] = u'பீ'
    table[u'pu'] = u'பு'
    table[u'pū'] = u'பூ'
    table[u'pe'] = u'பெ'
    table[u'pē'] = u'பே'
    table[u'pai'] = u'பை'
    table[u'po'] = u'பொ'
    table[u'pō'] = u'போ'
    table[u'pau'] = u'பௌ'
    table[u'ṟa'] = u'ற'
    table[u'iṟ'] = u'ற்'
    table[u'ṟā'] = u'றா'
    table[u'ṟi'] = u'றி'
    table[u'ṟī'] = u'றீ'
    table[u'ṟu'] = u'று'
    table[u'ṟū'] = u'றூ'
    table[u'ṟe'] = u'றெ'
    table[u'ṟē'] = u'றே'
    table[u'ṟai'] = u'றை'
    table[u'ṟo'] = u'றொ'
    table[u'ṟō'] = u'றோ'
    table[u'ṟau'] = u'றௌ'
    table[u'ña'] = u'ஞ'
    table[u'iñ'] = u'ஞ்'
    table[u'ñā'] = u'ஞா'
    table[u'ñi'] = u'ஞி'
    table[u'ñī'] = u'ஞீ'
    table[u'ñu'] = u'ஞு'
    table[u'ñū'] = u'ஞூ'
    table[u'ñe'] = u'ஞெ'
    table[u'ñē'] = u'ஞே'
    table[u'ñai'] = u'ஞை'
    table[u'ño'] = u'ஞொ'
    table[u'ñō'] = u'ஞோ'
    table[u'ñau'] = u'ஞௌ'
    table[u'ṅa'] = u'ங'
    table[u'iṅ'] = u'ங்'
    table[u'ṅā'] = u'ஙா'
    table[u'ṅi'] = u'ஙி'
    table[u'ṅī'] = u'ஙீ'
    table[u'ṅu'] = u'ஙு'
    table[u'ṅū'] = u'ஙூ'
    table[u'ṅe'] = u'ஙெ'
    table[u'ṅē'] = u'ஙே'
    table[u'ṅai'] = u'ஙை'
    table[u'ṅo'] = u'ஙொ'
    table[u'ṅō'] = u'ஙோ'
    table[u'ṅau'] = u'ஙௌ'
    table[u'ṇa'] = u'ண'
    table[u'iṇ'] = u'ண்'
    table[u'ṇā'] = u'ணா'
    table[u'ṇi'] = u'ணி'
    table[u'ṇī'] = u'ணீ'
    table[u'ṇu'] = u'ணு'
    table[u'ṇū'] = u'ணூ'
    table[u'ṇe'] = u'ணெ'
    table[u'ṇē'] = u'ணே'
    table[u'ṇai'] = u'ணை'
    table[u'ṇo'] = u'ணொ'
    table[u'ṇō'] = u'ணோ'
    table[u'ṇau'] = u'ணௌ'
    table[u'na'] = u'ந'
    table[u'in'] = u'ந்'
    table[u'nā'] = u'நா'
    table[u'ni'] = u'நி'
    table[u'nī'] = u'நீ'
    table[u'nu'] = u'நு'
    table[u'nū'] = u'நூ'
    table[u'ne'] = u'நெ'
    table[u'nē'] = u'நே'
    table[u'nai'] = u'நை'
    table[u'no'] = u'நொ'
    table[u'nō'] = u'நோ'
    table[u'nau'] = u'நௌ'
    table[u'ma'] = u'ம'
    table[u'im'] = u'ம்'
    table[u'mā'] = u'மா'
    table[u'mi'] = u'மி'
    table[u'mī'] = u'மீ'
    table[u'mu'] = u'மு'
    table[u'mū'] = u'மூ'
    table[u'me'] = u'மெ'
    table[u'mē'] = u'மே'
    table[u'mai'] = u'மை'
    table[u'mo'] = u'மொ'
    table[u'mō'] = u'மோ'
    table[u'mau'] = u'மௌ'
    table[u'ṉa'] = u'ன'
    table[u'iṉ'] = u'ன்'
    table[u'ṉā'] = u'னா'
    table[u'ṉi'] = u'னி'
    table[u'ṉī'] = u'னீ'
    table[u'ṉu'] = u'னு'
    table[u'ṉū'] = u'னூ'
    table[u'ṉe'] = u'னெ'
    table[u'ṉē'] = u'னே'
    table[u'ṉai'] = u'னை'
    table[u'ṉo'] = u'னொ'
    table[u'ṉō'] = u'னோ'
    table[u'ṉau'] = u'னௌ'
    table[u'ya'] = u'ய'
    table[u'iy'] = u'ய்'
    table[u'yā'] = u'யா'
    table[u'yi'] = u'யி'
    table[u'yī'] = u'யீ'
    table[u'yu'] = u'யு'
    table[u'yū'] = u'யூ'
    table[u'ye'] = u'யெ'
    table[u'yē'] = u'யே'
    table[u'yai'] = u'யை'
    table[u'yo'] = u'யொ'
    table[u'yō'] = u'யோ'
    table[u'yau'] = u'யௌ'
    table[u'ra'] = u'ர'
    table[u'ir'] = u'ர்'
    table[u'rā'] = u'ரா'
    table[u'ri'] = u'ரி'
    table[u'rī'] = u'ரீ'
    table[u'ru'] = u'ரு'
    table[u'rū'] = u'ரூ'
    table[u're'] = u'ரெ'
    table[u'rē'] = u'ரே'
    table[u'rai'] = u'ரை'
    table[u'ro'] = u'ரொ'
    table[u'rō'] = u'ரோ'
    table[u'rau'] = u'ரௌ'
    table[u'la'] = u'ல'
    table[u'il'] = u'ல்'
    table[u'lā'] = u'லா'
    table[u'li'] = u'லி'
    table[u'lī'] = u'லீ'
    table[u'lu'] = u'லு'
    table[u'lū'] = u'லூ'
    table[u'le'] = u'லெ'
    table[u'lē'] = u'லே'
    table[u'lai'] = u'லை'
    table[u'lo'] = u'லொ'
    table[u'lō'] = u'லோ'
    table[u'lau'] = u'லௌ'
    table[u'va'] = u'வ'
    table[u'iv'] = u'வ்'
    table[u'vā'] = u'வா'
    table[u'vi'] = u'வி'
    table[u'vī'] = u'வீ'
    table[u'vu'] = u'வு'
    table[u'vū'] = u'வூ'
    table[u've'] = u'வெ'
    table[u'vē'] = u'வே'
    table[u'vai'] = u'வை'
    table[u'vo'] = u'வொ'
    table[u'vō'] = u'வோ'
    table[u'vau'] = u'வௌ'
    table[u'ḷa'] = u'ழ'
    table[u'iḷ'] = u'ழ்'
    table[u'ḷā'] = u'ழா'
    table[u'ḷi'] = u'ழி'
    table[u'ḷī'] = u'ழீ'
    table[u'ḷu'] = u'ழு'
    table[u'ḷū'] = u'ழூ'
    table[u'ḷe'] = u'ழெ'
    table[u'ḷē'] = u'ழே'
    table[u'ḷai'] = u'ழை'
    table[u'ḷo'] = u'ழொ'
    table[u'ḷō'] = u'ழோ'
    table[u'ḷau'] = u'ழௌ'
    table[u'ḻa'] = u'ள'
    table[u'iḻ'] = u'ள்'
    table[u'ḻā'] = u'ளா'
    table[u'ḻi'] = u'ளி'
    table[u'ḻī'] = u'ளீ'
    table[u'ḻu'] = u'ளு'
    table[u'ḻū'] = u'ளூ'
    table[u'ḻe'] = u'ளெ'
    table[u'ḻē'] = u'ளே'
    table[u'ḻai'] = u'ளை'
    table[u'ḻo'] = u'ளொ'
    table[u'ḻō'] = u'ளோ'
    table[u'ḻau'] = u'ளௌ'
