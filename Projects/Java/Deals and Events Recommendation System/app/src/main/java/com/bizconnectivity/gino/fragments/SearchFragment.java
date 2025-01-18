package com.bizconnectivity.gino.fragments;

import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.support.annotation.Nullable;
import android.support.design.widget.CoordinatorLayout;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.arlib.floatingsearchview.FloatingSearchView;
import com.arlib.floatingsearchview.suggestions.model.SearchSuggestion;
import com.bizconnectivity.gino.R;
import com.bizconnectivity.gino.activities.OfferDetailActivity;
import com.bizconnectivity.gino.adapters.SearchResultsListAdapter;
import com.bizconnectivity.gino.asynctasks.SearchDealAsyncTask;
import com.bizconnectivity.gino.models.Deal;

import java.util.ArrayList;
import java.util.List;

import butterknife.BindView;
import butterknife.ButterKnife;

import static android.app.Activity.RESULT_OK;
import static com.bizconnectivity.gino.Common.isNetworkAvailable;
import static com.bizconnectivity.gino.Common.snackBar;
import static com.bizconnectivity.gino.Constant.ERR_MSG_NO_INTERNET_CONNECTION;
import static com.bizconnectivity.gino.Constant.ERR_MSG_NO_RECORD;

public class SearchFragment extends Fragment implements SearchResultsListAdapter.AdapterCallBack, SearchDealAsyncTask.AsyncResponse {

    @BindView(R.id.toolbar)
    Toolbar mToolbar;

    @BindView(R.id.floating_search_view)
    FloatingSearchView mSearchView;

    @BindView(R.id.search_results_list)
    RecyclerView mRecyclerViewSearch;

    @BindView(R.id.text_message)
    TextView mTextViewMessage;

    @BindView(R.id.coordinator_layout)
    CoordinatorLayout mCoordinatorLayout;

    private static final int SPEECH_REQUEST_CODE = 0;
    private SearchResultsListAdapter mSearchResultsAdapter;
    private List<Deal> dealLists = new ArrayList<>();

    public SearchFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_search, container, false);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {

        super.onViewCreated(view, savedInstanceState);

        // Layout Binding
        ButterKnife.bind(this, view);

        // Action Bar
        ((AppCompatActivity) getActivity()).setSupportActionBar(mToolbar);

        // Setup Search Bar
        setupSearchBar();

        // Setup RecycleView
        mSearchResultsAdapter = new SearchResultsListAdapter(dealLists, this);
        mRecyclerViewSearch.setAdapter(mSearchResultsAdapter);
        mRecyclerViewSearch.setLayoutManager(new LinearLayoutManager(getContext()));

        if (isNetworkAvailable(getContext())) {
            mTextViewMessage.setText("Search Gino");
            mTextViewMessage.setVisibility(View.VISIBLE);
            mRecyclerViewSearch.setVisibility(View.GONE);
        } else {
            mTextViewMessage.setText(ERR_MSG_NO_INTERNET_CONNECTION);
            mTextViewMessage.setVisibility(View.VISIBLE);
            mRecyclerViewSearch.setVisibility(View.GONE);
        }
    }

    private void setupSearchBar() {

        // Search Suggestion
//        mSearchView.setOnQueryChangeListener(new FloatingSearchView.OnQueryChangeListener() {
//            @Override
//            public void onSearchTextChanged(String oldQuery, String newQuery) {
//
//                if (!oldQuery.equals("") && newQuery.equals("")) {
//
//                    mSearchView.clearSuggestions();
//
//                } else {
//
//                    //this shows the top left circular progress
//                    //you can call it where ever you want, but
//                    //it makes sense to do it when loading something in
//                    //the background.
//                    mSearchView.showProgress();
//
//                    //simulates a query call to a data source
//                    //with a new query.
//                }
//            }
//        });

//        mSearchView.setOnFocusChangeListener(new FloatingSearchView.OnFocusChangeListener() {
//            @Override
//            public void onFocus() {
//
//                //show suggestions when search bar gains focus (typically history suggestions)
//                mSearchView.swapSuggestions(DataHelper.getHistory(getActivity(), 5));
//            }
//
//            @Override
//            public void onFocusCleared() {
//
//                //set the title of the bar so that when focus is returned a new query begins
//                mSearchView.setSearchBarTitle(spokenText);
//
//                //you can also set setSearchText(...) to make keep the query there when not focused and when focus returns
//                //mSearchView.setSearchText(searchSuggestion.getBody());
//
//                Log.d(TAG, "onFocusCleared()");
//            }
//        });


//        mSearchView.setOnBindSuggestionCallback(new SearchSuggestionsAdapter.OnBindSuggestionCallback() {
//            @Override
//            public void onBindSuggestion(View suggestionView, ImageView leftIcon,
//                                         TextView textView, SearchSuggestion item, int itemPosition) {

//                DealSearchSuggestion colorSuggestion = (DealSearchSuggestion) item;

//                String textColor = mIsDarkSearchTheme ? "#ffffff" : "#000000";
//                String textLight = mIsDarkSearchTheme ? "#bfbfbf" : "#787878";

//                if (colorSuggestion.getIsHistory()) {
//                    leftIcon.setImageDrawable(ResourcesCompat.getDrawable(getResources(),
//                            R.drawable.ic_history_black_24dp, null));

//                    Util.setIconColor(leftIcon, Color.parseColor(textColor));
//                    leftIcon.setAlpha(.36f);
//                } else {
//                    leftIcon.setAlpha(0.0f);
//                    leftIcon.setImageDrawable(null);
//                }

//                textView.setTextColor(Color.parseColor(textColor));
//                String text = colorSuggestion.getBody()
//                        .replaceFirst(mSearchView.getQuery(),
//                                "<font color=\"" + textLight + "\">" + mSearchView.getQuery() + "</font>");
//                textView.setText(Html.fromHtml(text));
//            }
//        });



        // Menu Item Click
        mSearchView.setOnMenuItemClickListener(new FloatingSearchView.OnMenuItemClickListener() {
            @Override
            public void onActionMenuItemSelected(MenuItem item) {

                if (item.getItemId() == R.id.action_voice) {

                    Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
                    intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
                    startActivityForResult(intent, SPEECH_REQUEST_CODE);
                }
            }
        });

        mSearchView.setOnSearchListener(new FloatingSearchView.OnSearchListener() {

            @Override
            public void onSuggestionClicked(SearchSuggestion searchSuggestion) {

            }

            @Override
            public void onSearchAction(String currentQuery) {

                if (currentQuery.isEmpty()) {

                    mTextViewMessage.setText(ERR_MSG_NO_RECORD);
                    mTextViewMessage.setVisibility(View.VISIBLE);
                    mRecyclerViewSearch.setVisibility(View.GONE);

                } else {

                    if (isNetworkAvailable(getContext())) {

                        mSearchView.showProgress();

                        new SearchDealAsyncTask(SearchFragment.this, currentQuery).execute();

                    } else {

                        snackBar(mCoordinatorLayout, ERR_MSG_NO_INTERNET_CONNECTION);
                    }
                }
            }
        });
    }

    // Retrieve Search Deal
    @Override
    public void retrieveSearchDeal(List<Deal> result) {

        if (result.isEmpty()) {

            mTextViewMessage.setText(ERR_MSG_NO_RECORD);
            mTextViewMessage.setVisibility(View.VISIBLE);
            mRecyclerViewSearch.setVisibility(View.GONE);

        } else {

            mTextViewMessage.setVisibility(View.GONE);
            mRecyclerViewSearch.setVisibility(View.VISIBLE);
            dealLists = result;
            mSearchResultsAdapter.swapData(dealLists);
        }

        mSearchView.hideProgress();
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {

        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == SPEECH_REQUEST_CODE && resultCode == RESULT_OK) {

            List<String> results = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);
            final String spokenText = results.get(0);


            getActivity().runOnUiThread(new Runnable() {
                public void run() {
                    //Do something on UiThread
                    mSearchView.setSearchText(spokenText);
                }
            });

//            Log.d("TAG", "onActivityResult: " + spokenText);
//
//            if (spokenText.isEmpty()) {
//
////                mTextViewMessage.setText(ERR_MSG_NO_RECORD);
////                mTextViewMessage.setVisibility(View.VISIBLE);
////                mRecyclerViewSearch.setVisibility(View.GONE);
//
//            } else {
//
//                // Search spoken text
//                if (isNetworkAvailable(getContext())) {
//
////                    mSearchView.showProgress();
//
//                    new SearchDealAsyncTask(spokenText).execute();
//
//                } else {
//
////                    snackBar(mCoordinatorLayout, ERR_MSG_NO_INTERNET_CONNECTION);
//                }
//            }
        }
    }

    // Deal OnClick
    @Override
    public void adapterOnClick(int adapterPosition) {
        Intent intent = new Intent(getContext(), OfferDetailActivity.class);
        intent.putExtra("POSITION", dealLists.get(adapterPosition).getDealID());
        startActivity(intent);
    }

    @Override
    public void onResume(){
        super.onResume();
    }
}

