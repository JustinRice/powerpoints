
def readGames(teams):
    dataFile = open("games",'r')
    outfile = open("output.txt","w")
    doneReading = False
    listedTeams = []
    exclude = ["Washington(MD)","Victory Christian(VA)"]
    gameCount = 1
    while not doneReading:
        line = dataFile.readline()
        if line.strip() == "*****":
            doneReading = True
        else:
            line = line.strip();
            lineList = line.split("@")
            if (lineList[2][0:9] != "Untracked") and (lineList[3][0:9] != "Untracked") and (lineList[2] not in exclude) and (lineList[3] not in exclude):
                makeGame(lineList, teams, gameCount,outfile)
                gameCount += 1
    dataFile.close()
    outfile.close()

def makeGame(lineList, teams, gameCount,outfile):
    homeID = teams[lineList[2]]
    roadID = teams[lineList[3]]
    year = lineList[1][-4:]
    day = 0;
    month = 0;
    if len(lineList[1]) == 8:
        month = lineList[1][:2]
        day = lineList[1][2:4]
    else:
        month = str(0)+ str(lineList[1][:1])
        day = lineList[1][1:3]
    date = str(day) + " " + str(month) + " " + str(year)
    dist = "N"
    if lineList[7].strip()== "True":
        dist = "Y"
    outfile.write("insert into games (homeID, awayID, day, dist) values (" + str(homeID) + "," + str(roadID) + "," + "to_date('"+ str(date) + "', 'DD MM YYYY')," + "'" + dist + "');\n")
    week = lineList[5];
    outfile.write("update teams set week" + str(week) + "=" + str(gameCount) + " where id=" + str(homeID) + " or id=" + str(roadID) + ";\n")


# Main

teams = {'Albemarle' : 1
,
'Annandale' : 2
,
'Atlee' : 3
,
'Battlefield' : 4
,
'Bayside' : 5
,
'Bethel' : 6
,
'Briar Woods' : 7
,
'Broad Run' : 8
,
'Brooke Point' : 9
,
'Caroline' : 10
,
'Centreville' : 11
,
'Chancellor' : 12
,
'Chantilly' : 13
,
'Churchland' : 14
,
'Colonial Forge' : 15
,
'Cosby' : 16
,
'Courtland' : 17
,
'Frank Cox' : 18
,
'Clover Hill' : 19
,
'Deep Creek' : 20
,
'Deep Run' : 21
,
'Denbigh' : 22
,
'Dinwiddie' : 23
,
'Douglas Freeman' : 24
,
'Eastern View' : 25
,
'Fairfax' : 26
,
'Falls Church' : 27
,
'First Colonial' : 28
,
'Forest Park' : 29
,
'Franklin County' : 30
,
'Freedom-PW' : 31
,
'Gar-Field' : 32
,
'George Marshall' : 33
,
'Glen Allen' : 34
,
'Gloucester' : 35
,
'Grafton' : 36
,
'Granby' : 37
,
'Grassfield' : 38
,
'Great Bridge' : 39
,
'Green Run' : 40
,
'Halifax' : 41
,
'Hampton' : 42
,
'Hanover' : 43
,
'Hayfield' : 44
,
'Henrico' : 45
,
'Heritage-NN' : 46
,
'Hermitage' : 47
,
'Herndon' : 48
,
'Hickory' : 49
,
'Highland Springs' : 50
,
'Huguenot' : 51
,
'Hylton' : 52
,
'Indian River' : 53
,
'J.R. Tucker' : 54
,
'James Madison' : 55
,
'James River-Ch.' : 56
,
'Robinson' : 57
,
'Jamestown' : 58
,
'JEB Stuart' : 59
,
'Kecoughtan' : 60
,
'Floyd Kellam' : 61
,
'Kempsville' : 62
,
'King George' : 63
,
"King's Fork" : 64
,
'L.C. Bird' : 65
,
'Lake Taylor' : 66
,
'Lafayette' : 67
,
'Lake Braddock' : 68
,
'Landstown' : 69
,
'Langley' : 70
,
'Lee-Davis' : 71
,
'Louisa' : 72
,
'Manchester' : 73
,
'Massaponax' : 74
,
'Matoaca' : 75
,
'Maury' : 76
,
'McLean' : 77
,
'Meadowbrook' : 78
,
'Menchville' : 79
,
'Midlothian' : 80
,
'Mills Godwin' : 81
,
'Monacan' : 82
,
'Mount Vernon' : 83
,
'Mountain View' : 84
,
'Nansemond River' : 85
,
'North Stafford' : 86
,
'Norview' : 87
,
'Oakton' : 88
,
'Ocean Lakes' : 89
,
'Orange' : 90
,
'Osbourn' : 91
,
'Osbourn Park' : 92
,
'Oscar Smith' : 93
,
'Patrick Henry-Ash' : 94
,
'Patrick Henry-Roa' : 95
,
'Patriot' : 96
,
'Potomac' : 97
,
'Potomac Falls' : 98
,
'Powhatan' : 99
,
'Prince George' : 100
,
'Princess Anne' : 101
,
'R.E. Lee-Spr' : 102
,
'Riverbend' : 103
,
'Salem' : 104
,
'Smithfield' : 105
,
'South County' : 106
,
'South Lakes' : 107
,
'Stafford' : 108
,
'Stone Bridge' : 109
,
'Stonewall Jackson' : 110
,
'Tallwood' : 111
,
'T.C. Williams' : 112
,
'T. Jefferson-A' : 113
,
'Thomas Dale' : 114
,
'Thomas Edison' : 115
,
'Tuscarora' : 116
,
'Varina' : 117
,
'W.T. Woodson' : 118
,
'Wakefield' : 119
,
'Warwick' : 120
,
'Washington-Lee' : 121
,
'West Potomac' : 122
,
'West Springfield' : 123
,
'Western Branch' : 124
,
'Westfield' : 125
,
'Woodbridge' : 126
,
'Woodrow Wilson' : 127
,
'Woodside' : 128
,
'Yorktown' : 129
,
'William Byrd' : 130
,
'William Fleming' : 131
,
'John Champe' : 132
,
'Dominion' : 133
,
'Freedom-SR' : 134
,
'Heritage-LC' : 135
,
'Loudoun County' : 136
,
'Loudoun Valley' : 137
,
'Park View-St' : 138
,
'Rock Ridge' : 139
,
'Woodgrove' : 140
,
'Fauquier' : 141
,
'Kettle Run' : 142
,
'Liberty' : 143
,
'Charlottesville' : 144
,
'John Handley' : 145
,
'Millbrook' : 146
,
'Sherando' : 147
,
'James Wood' : 148
,
'Bassett' : 149
,
'George Washington' : 150
,
'Pulaski' : 151
,
'Salem-S' : 152
,
'Carroll County' : 153
,
'Amherst' : 154
,
'E.C. Glass' : 155
,
'Jefferson Forest' : 156
,
'Liberty Christian' : 157
,
'Harrisonburg' : 158
,
'James Monroe' : 159
,
'Spotsylvania' : 160
,
'New Kent' : 161
,
'Poquoson' : 162
,
'Tabb' : 163
,
'Warhill' : 164
,
'York' : 165
,
'William Monroe' : 166
,
'Warren County' : 167
,
'Armstrong' : 168
,
'Colonial Heights' : 169
,
'Hopewell' : 170
,
'Petersburg' : 171
,
'T. Jefferson-Ri' : 172
,
'John Marshall' : 173
,
'George Wythe-Ri' : 174
,
'Riverside' : 175
,
'I.C. Norcom' : 176
,
'B.T. Washington' : 177
,
'Brentsville' : 178
,
'Culpeper' : 179
,
'Manassas Park' : 180
,
'Skyline' : 181
,
'Phoebus' : 182
,
'Lakeland' : 183
,
'Park View-SH' : 184
,
'Southampton' : 185
,
'Alleghany' : 186
,
'Lord Botetourt' : 187
,
'Northside' : 188
,
'Rockbridge Co.' : 189
,
'Staunton River' : 190
,
'Fluvanna' : 191
,
'Monticello' : 192
,
'Western Albemarle' : 193
,
'Patrick County' : 194
,
'Tunstall' : 195
,
'Magna Vista' : 196
,
'Blacksburg' : 197
,
'Cave Spring' : 198
,
'Christiansburg' : 199
,
'Hidden Valley' : 200
,
'Brookville' : 201
,
'Heritage-Lyn' : 202
,
'Liberty-Bed' : 203
,
'Rustburg' : 204
,
'Abingdon' : 205
,
'Broadway' : 206
,
'Fort Defiance' : 207
,
'Spotswood' : 208
,
'Turner Ashby' : 209
,
'Waynesboro' : 210
,
'Bruton' : 211
,
'Central-Wood' : 212
,
'Clarke County' : 213
,
'Madison County' : 214
,
'George Mason' : 215
,
'Strasburg' : 216
,
'Nelson County' : 217
,
'Acadia' : 218
,
'Nandua' : 219
,
'Amelia County' : 220
,
'Bluestone' : 221
,
'Goochland' : 222
,
'Nottoway' : 223
,
'Prince Edward' : 224
,
'Washington & Lee' : 225
,
'Buffalo Gap' : 226
,
'East Rockingham' : 227
,
'Page County' : 228
,
'Stuarts Draft' : 229
,
'Wilson Memorial' : 230
,
'King William' : 231
,
'Brunswick' : 232
,
'Greensville' : 233
,
'R.E. Lee-St' : 234
,
'Grundy' : 235
,
'Appomattox' : 236
,
'Chatham' : 237
,
'Dan River' : 238
,
'Gretna' : 239
,
'Marion' : 240
,
'Buckinham' : 241
,
'Randolph-Henry' : 242
,
'John Battle' : 243
,
'Central-Wise' : 244
,
'Gate City' : 245
,
'Lee' : 246
,
'Ridgeview' : 247
,
'Union' : 248
,
'Graham' : 249
,
'Grayson' : 250
,
'Martinsville' : 251
,
'James River-Bu' : 252
,
'Lebanon' : 253
,
'Richlands' : 254
,
'Tazewell' : 255
,
'Virginia' : 256
,
'Gate City' : 257
,
'Giles' : 258
,
'Glenvar' : 259
,
'Floyd County' : 260
,
'Altavista' : 261
,
'William Campbell' : 262
,
'Northampton' : 263
,
'Central-Lu' : 264
,
'Cumberland' : 265
,
'Colonial Beach' : 266
,
'Essex' : 267
,
'Lancaster' : 268
,
'Northumberland' : 269
,
'Rappahannock' : 270
,
'Stonewall Jackson-Qui' : 271
,
'Luray' : 272
,
'Riverheads' : 273
,
'Charles City' : 274
,
'King & Queen' : 275
,
'Mathews' : 276
,
'Middlesex' : 277
,
'West Point' : 278
,
'Franklin' : 279
,
'Surry County' : 280
,
'Susex Central' : 281
,
'Windsor' : 282
,
'Honaker' : 283
,
'Hurley' : 284
,
'Twin Valley' : 285
,
'J.I. Burton' : 286
,
'Castlewood' : 287
,
'Eastside' : 288
,
'Rye Cove' : 289
,
'Twin Springs' : 290
,
'Thomas Walker' : 291
,
'Chilhowie' : 292
,
'Patrick Henry-GS' : 293
,
'Holston' : 294
,
'Northwood' : 295
,
'Rural Retreat' : 296
,
'George Wythe-W' : 297
,
'Bland-Rocky Gap' : 298
,
'Fort Chiswell' : 299
,
'Galax' : 300
,
'Narrows' : 301
,
'Bath County' : 302
,
'Covington' : 303
,
'Craig County' : 304
,
'Parry McCluer' : 305
,
'Auburn' : 306
,
'Eastern Montgomery' : 307
,
'Radford' : 308
,
'Athens(NC)' : 309
,
'Northwestern(SC)' : 310
,
'Hillside(NC)' : 311
,
'Okeechobee(Fl)' : 312
,
'Vance(NC)' : 313
,
'Woodrow Wilson(DC)' : 314
,
'Alleghany(NC)' : 315
,
'Avalon School(MD)' : 316
,
'Col. Richardson(MD)' : 317
,
'East Hardy(WV)' : 318
,
'Greenbrier West(WV)' : 319
,
'Hancock Co.(TN)' : 320
,
'Harlan Independent(KY)' : 321
,
'Jenkins(KY)' : 322
,
'Montcalm(WV)' : 323
,
'North Stokes(NC)' : 324
,
'Paintsville(KY)' : 325,
'Pendleton(WV)' : 326
,
'Phelps(KY)' : 327
,
'Pocahontas(WV)' : 328
,
'Snow Hill(MD)' : 329
,
'South Floyd(KY)' : 330
,
'Unaka(TN)' : 331
,
'Van(WV)' : 332
,
'Weldon(NC)' : 333
,
'BroadWater Academy(VA)' : 334
,
'Charltote Christian(NC)' : 335
,
'Grace Christian' : 336
,
'Greenbriar Academy(VA)' : 337
,
'Kenston Forest(VA)' : 338
,
'Portsmouth Christian(VA)' : 339
,
'Quantico(VA)' : 340
,
'Roanoke Catholic(VA)' : 341
,
'Trinity Episcopal(VA)' : 342
,
'Word of God Christian(VA)' : 343
,
'Bartlett Yancey(NC)' : 344
,
'Cambridge/SDorchester(MD)' : 345
,
'Cocoa(Fl)' : 346
,
'Currituck(NC)' : 347
,
'Eastern(DC)' : 348
,
'First Flight(NC)' : 349
,
'Letcher Co (KY)' : 350
,
'McMichael(NC)' : 351
,
'Morehead(NC)' : 352
,
'Northeastern(NC)' : 353
,
'Potomac(MD)' : 354
,
'Roanoke Rapids(NC)' : 355
,
'Spring Mills(WV)' : 356
,
'Sullivan South(TN)' : 357
,
'Woodberry Forest(Va)' : 358
,
'Bluefield(WV)' : 359
,
'East Ridge(KY)' : 360
,
'Fort Hill(MD)' : 361
,
'Holmes(NC)' : 362
,
'Kent(MD)' : 363
,
'McCreary Centray(KY)' : 364
,
'River View(WV)' : 365
,
'Shelby Valley(KY)' : 366
,
'Benedictine College(VA)' : 367,
'Fork Union Mil-LCA(VA)' : 368
,
'Sain John Paul t Great(VA)' : 369
,
"St. Christopher's(VA)" : 370
,
'Rappahannock County' : 371
,
'Chincoteague' : 372
,
'JM Bennett(MD)' : 373
,
'Bisohp McNamara' : 374
,
'David Crockett(TN)' : 375
,
'Hedgesville(WV)' : 376
,
'Jefferson County(WV)' : 377
,
'Martinsburg(WV)' : 378
,
'Person(NC)' : 379
,
'Tennessee(TN)' : 380
,
'Washington(WV)' : 381}


readGames(teams)
